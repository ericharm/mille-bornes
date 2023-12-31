import pytest

from src.defs import cards
from src.defs.constants import SPEED_LIMIT
from src.defs.game import Condition
from src.domain import tableau as tableau_domain
from src.models.tableau import Tableau
from tests.utils.assertions import assert_exception_matches


def test_add_battle_hazard_to_tableau_success() -> None:
    go_card = cards.Go()
    tableau = Tableau(battle_cards=[go_card])
    flat_tire = cards.FlatTire()
    tableau_domain.add_card_to_tableau(tableau=tableau, card=flat_tire)
    assert tableau.battle_cards == [go_card, flat_tire]


def test_add_battle_hazard_to_empty_tableau() -> None:
    tableau = Tableau(battle_cards=[])
    flat_tire = cards.FlatTire()
    with pytest.raises(Exception) as exception:
        tableau_domain.add_card_to_tableau(tableau=tableau, card=flat_tire)

    assert_exception_matches(exception.value, Exception("Player has immunity against this hazard"))


def test_add_speed_limit_to_tableau_success() -> None:
    tableau = Tableau(battle_cards=[], speed_cards=[])
    speed_limit = cards.SpeedLimit()
    tableau_domain.add_card_to_tableau(tableau=tableau, card=speed_limit)
    assert tableau.speed_cards == [speed_limit]


def test_add_speed_limit_to_tableau_with_speed_limit_already_showing() -> None:
    already_played_speed_limit = cards.SpeedLimit()
    tableau = Tableau(battle_cards=[], speed_cards=[already_played_speed_limit])
    new_speed_limit = cards.SpeedLimit()

    with pytest.raises(Exception) as exception:
        tableau_domain.add_card_to_tableau(tableau=tableau, card=new_speed_limit)

    assert tableau.speed_cards == [already_played_speed_limit]
    assert_exception_matches(exception.value, Exception("Player has immunity against this hazard"))


def test_add_battle_remedy_to_tableau_success() -> None:
    go = cards.Go()
    accident = cards.Accident()
    tableau = Tableau(battle_cards=[go, accident], speed_cards=[])
    repairs = cards.Repairs()
    tableau_domain.add_card_to_tableau(tableau=tableau, card=repairs)

    assert tableau.battle_cards == [go, accident, repairs]


def test_add_battle_remedy_to_tableau_failure() -> None:
    go = cards.Go()
    accident = cards.Accident()
    tableau = Tableau(battle_cards=[go, accident], speed_cards=[])
    gasoline = cards.Gasoline()

    with pytest.raises(Exception) as exception:
        tableau_domain.add_card_to_tableau(tableau=tableau, card=gasoline)

    assert_exception_matches(exception.value, Exception("Player does not have this condition"))

    assert tableau.battle_cards == [go, accident]


def test_add_end_of_limit_to_tableau_success() -> None:
    speed_limit = cards.SpeedLimit()
    tableau = Tableau(battle_cards=[], speed_cards=[speed_limit])
    assert tableau.speed_limit == SPEED_LIMIT

    end_of_limit = cards.EndOfLimit()
    tableau_domain.add_card_to_tableau(tableau=tableau, card=end_of_limit)

    assert tableau.speed_cards == [speed_limit, end_of_limit]
    assert tableau.speed_limit is None


def test_add_end_of_limit_to_tableau_failure() -> None:
    tableau = Tableau(battle_cards=[], speed_cards=[])
    assert tableau.speed_limit is None

    end_of_limit = cards.EndOfLimit()

    with pytest.raises(Exception) as exception:
        tableau_domain.add_card_to_tableau(tableau=tableau, card=end_of_limit)

    assert tableau.speed_limit is None
    assert_exception_matches(exception.value, Exception("Player does not have this condition"))


def test_add_go_to_tableau_with_empty_battle_pile() -> None:
    go = cards.Go()
    tableau = Tableau(battle_cards=[])
    tableau_domain.add_card_to_tableau(tableau=tableau, card=go)
    assert tableau.battle_cards == [go]


def test_add_go_to_tableau_showing_stop() -> None:
    original_go = cards.Go()
    stop = cards.Stop()
    tableau = Tableau(battle_cards=[original_go, stop])
    new_go = cards.Go()
    tableau_domain.add_card_to_tableau(tableau=tableau, card=new_go)
    assert tableau.battle_cards == [original_go, stop, new_go]


def test_add_go_to_tableau_showing_non_stop_hazard() -> None:
    original_go = cards.Go()
    accident = cards.Accident()
    tableau = Tableau(battle_cards=[original_go, accident])
    new_go = cards.Go()
    with pytest.raises(Exception) as exception:
        tableau_domain.add_card_to_tableau(tableau=tableau, card=new_go)

    assert_exception_matches(exception.value, Exception("Player cannot play Go card"))
    assert tableau.battle_cards == [original_go, accident]


def test_add_go_to_tableau_showing_go() -> None:
    original_go = cards.Go()
    tableau = Tableau(battle_cards=[original_go])
    new_go = cards.Go()

    with pytest.raises(Exception) as exception:
        tableau_domain.add_card_to_tableau(tableau=tableau, card=new_go)

    assert_exception_matches(exception.value, Exception("Player cannot play Go card"))
    assert tableau.battle_cards == [original_go]


def test_add_go_to_tableau_showing_other_remedy() -> None:
    go = cards.Go()
    accident = cards.Accident()
    repairs = cards.Repairs()
    tableau = Tableau(battle_cards=[go, accident, repairs])
    new_go = cards.Go()
    tableau_domain.add_card_to_tableau(tableau=tableau, card=new_go)
    assert tableau.battle_cards == [go, accident, repairs, new_go]


def test_add_distance_card_to_tableau_success() -> None:
    tableau = Tableau(battle_cards=[cards.Go()], distance_cards=[])
    distance_100 = cards.Distance100()
    tableau_domain.add_card_to_tableau(tableau=tableau, card=distance_100)
    assert tableau.distance_cards == [distance_100]


def test_add_distance_card_to_tableau_not_showing_go() -> None:
    tableau = Tableau(battle_cards=[], distance_cards=[])
    distance_100 = cards.Distance100()
    with pytest.raises(Exception) as exception:
        tableau_domain.add_card_to_tableau(tableau=tableau, card=distance_100)

    assert_exception_matches(
        exception.value, Exception("Player cannot play distance card when Go is not showing")
    )


def test_add_distance_card_to_tableau_beyond_speed_limit() -> None:
    tableau = Tableau(
        battle_cards=[cards.Go()], distance_cards=[], speed_cards=[cards.SpeedLimit()]
    )
    distance_200 = cards.Distance200()
    with pytest.raises(Exception) as exception:
        tableau_domain.add_card_to_tableau(tableau=tableau, card=distance_200)

    assert_exception_matches(
        exception.value, Exception("Cannot play distance card beyond speed limit")
    )
    assert tableau.distance_cards == []


def test_add_distance_card_to_tableau_within_speed_limit() -> None:
    tableau = Tableau(
        battle_cards=[cards.Go()], distance_cards=[], speed_cards=[cards.SpeedLimit()]
    )
    distance_50 = cards.Distance50()
    tableau_domain.add_card_to_tableau(tableau=tableau, card=distance_50)
    assert tableau.distance_cards == [distance_50]


def test_add_safety_card_to_tableau() -> None:
    driving_ace = cards.DrivingAce()
    tableau = Tableau(safety_cards=[])
    tableau_domain.add_card_to_tableau(tableau=tableau, card=driving_ace)
    assert tableau.safety_cards == [driving_ace]
    assert Condition.accident in tableau.immunities
