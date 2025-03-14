import pytest

from src.defs import cards as cards
from src.defs.card_types import Card
from src.defs.constants import SPEED_LIMIT, TOTAL_CARD_COUNT
from src.defs.game import Condition
from src.domain import cards as cards_domain
from tests.utils.assertions import assert_exception_matches


def test_create_deck() -> None:
    deck = cards_domain.create_deck()
    assert len(deck) == TOTAL_CARD_COUNT


def test_get_top_card() -> None:
    deck = cards_domain.create_deck()
    top_card = cards_domain.get_top_card(deck)
    assert top_card == deck.pop()


def test_get_top_card_from_empty_deck() -> None:
    deck: list[Card] = []
    assert cards_domain.get_top_card(deck) is None


def test_safety_card_cures_condition() -> None:
    extra_tank = cards.ExtraTank()
    assert cards_domain.safety_card_cures_condition(extra_tank, Condition.out_of_gas) is True


def test_right_of_way_cures_two_conditions() -> None:
    right_of_way = cards.RightOfWay()

    with pytest.raises(Exception) as exception:
        _ = right_of_way.condition

    assert_exception_matches(
        exception.value,
        Exception(
            "Unsafe call to 'condition' on SafetyCard: some safety cards have multiple conditions"
        ),
    )

    assert cards_domain.safety_card_cures_condition(right_of_way, Condition.speed_limit) is True
    assert cards_domain.safety_card_cures_condition(right_of_way, Condition.stop) is True


def test_safety_card_does_not_cure_condition() -> None:
    extra_tank = cards.ExtraTank()
    accident = Condition.accident
    assert not cards_domain.safety_card_cures_condition(extra_tank, accident)


def test_find_safety_card_in_hand() -> None:
    extra_tank = cards.ExtraTank()
    out_of_gas = cards.OutOfGas()
    gasoline = cards.Gasoline()
    hand: list[Card] = [extra_tank, out_of_gas, gasoline]
    assert cards_domain.find_safety_card_in_hand(hand) == extra_tank


def test_find_go_card_in_hand() -> None:
    driving_ace = cards.DrivingAce()
    go = cards.Go()
    stop = cards.Stop()
    hand: list[Card] = [driving_ace, go, stop]
    assert cards_domain.find_go_card_in_hand(hand) == go


def test_find_end_of_limit_card_in_hand() -> None:
    speed_limit = cards.SpeedLimit()
    right_of_way = cards.RightOfWay()
    end_of_limit = cards.EndOfLimit()
    hand: list[Card] = [speed_limit, right_of_way, end_of_limit]
    assert cards_domain.find_end_of_limit_card_in_hand(hand) == end_of_limit


def test_find_remedy_card_in_hand() -> None:
    spare_tire = cards.SpareTire()
    puncture_proof = cards.PunctureProof()
    flat_tire = cards.FlatTire()
    hand: list[Card] = [spare_tire, puncture_proof, flat_tire]
    assert cards_domain.find_remedy_card_in_hand(hand, Condition.flat_tire) == spare_tire


def test_find_remedy_card_not_in_hand() -> None:
    go = cards.Go()
    puncture_proof = cards.PunctureProof()
    flat_tire = cards.FlatTire()
    hand: list[Card] = [go, puncture_proof, flat_tire]
    assert cards_domain.find_remedy_card_in_hand(hand, Condition.flat_tire) is None


def test_find_longest_distance_card_in_hand() -> None:
    distance_25 = cards.Distance25()
    distance_50 = cards.Distance50()
    distance_75 = cards.Distance75()
    hand: list[Card] = [distance_25, distance_50, distance_75]
    assert cards_domain.find_longest_distance_card_in_hand(hand, None) == distance_75


def test_find_longest_distance_card_in_hand_with_speed_limit_playable() -> None:
    distance_25 = cards.Distance25()
    distance_50 = cards.Distance50()
    distance_75 = cards.Distance75()
    hand: list[Card] = [distance_25, distance_50, distance_75]
    assert cards_domain.find_longest_distance_card_in_hand(hand, SPEED_LIMIT) == distance_50


def test_find_longest_distance_card_in_hand_with_speed_limit_not_playable() -> None:
    distance_75 = cards.Distance75()
    distance_100 = cards.Distance100()
    distance_200 = cards.Distance200()
    hand: list[Card] = [distance_75, distance_100, distance_200]
    assert cards_domain.find_longest_distance_card_in_hand(hand, SPEED_LIMIT) is None


def test_find_longest_distance_card_in_hand_with_no_distance_cards() -> None:
    go = cards.Go()
    puncture_proof = cards.PunctureProof()
    flat_tire = cards.FlatTire()
    hand: list[Card] = [go, puncture_proof, flat_tire]
    assert cards_domain.find_longest_distance_card_in_hand(hand, None) is None


@pytest.mark.parametrize(
    "card, target_is_self",
    [
        (cards.Go(), True),
        (cards.EndOfLimit(), True),
        (cards.SpeedLimit(), False),
        (cards.RightOfWay(), True),
        (cards.Stop(), False),
        (cards.OutOfGas(), False),
        (cards.FlatTire(), False),
        (cards.Accident(), False),
    ],
)
def test_card_target_is_self(card: Card, target_is_self: bool) -> None:
    assert cards_domain.card_target_is_self(card) == target_is_self
