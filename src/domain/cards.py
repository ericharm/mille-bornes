from typing import Callable, Optional, cast
from src.defs.card_names import CardName
from src.defs.card_types import Card, CardType, HazardCard, RemedyCard, SafetyCard
from src.defs.constants import CARD_COUNTS_BY_CARD_TYPE
from src.defs.game import Condition


def create_deck() -> list[Card]:
    cards = []
    for card_type in CARD_COUNTS_BY_CARD_TYPE.keys():
        count = CARD_COUNTS_BY_CARD_TYPE[card_type]
        for _ in range(count):
            cards.append(card_type())

    return cards


def get_top_card(cards: list[Card]) -> Optional[Card]:
    return cards[-1] if len(cards) else None


def remedy_cures_hazard(remedy: Condition, hazard: Condition) -> bool:
    return remedy == hazard


def remedy_card_cures_hazard_card(remedy_card: RemedyCard, hazard_card: Card) -> bool:
    for remedy in remedy_card.value:
        for condition in cast(HazardCard, hazard_card).value:
            if not remedy_cures_hazard(remedy, condition):
                return False
    return True


def safety_card_cures_condition(safety_card: SafetyCard, condition: Condition) -> bool:
    for concern in safety_card.value:
        if concern == condition:
            return True
    return False


def card_meets_condition(card: Card, condition: Callable[[Card], bool]) -> bool:
    return condition(card)


def find_cards_in_hand(hand: list[Card], condition: Callable) -> list[Card]:
    return [card for card in hand if card_meets_condition(card, condition)]


def find_card_in_hand(hand: list[Card], condition: Callable) -> Optional[Card]:
    cards = find_cards_in_hand(hand, condition)
    return cards[0] if len(cards) else None


def find_safety_card_in_hand(
    hand: list[Card], concern: Optional[Condition] = None
) -> Optional[Card]:
    if concern:
        return find_card_in_hand(
            hand, lambda card: card.card_type == CardType.safety and concern in card.value
        )
    return find_card_in_hand(hand, lambda card: card.card_type == CardType.safety)


def card_is_go_card(card: Card) -> bool:
    return card.name == CardName.go


def find_go_card_in_hand(hand: list[Card]) -> Optional[Card]:
    return find_card_in_hand(hand, card_is_go_card)


def find_end_of_limit_card_in_hand(hand: list[Card]) -> Optional[Card]:
    return find_card_in_hand(hand, lambda card: card.name == CardName.end_of_limit)


def find_longest_distance_card_in_hand(hand: list[Card]) -> Optional[Card]:
    distance_cards = find_cards_in_hand(hand, lambda card: card.card_type == CardType.distance)
    sorted_cards = sorted(distance_cards, key=lambda card: card.value, reverse=True)
    return sorted_cards[0] if len(sorted_cards) else None


def card_is_played_to_own_tableau(card: Card) -> bool:
    return card.card_type != CardType.hazard


def card_is_played_to_opponent_tableau(card: Card) -> bool:
    return not card_is_played_to_own_tableau(card)
