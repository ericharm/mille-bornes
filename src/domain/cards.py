import random
from typing import Optional, cast

from src.defs.card_names import CardName
from src.defs.card_types import Card, CardType, DistanceCard, RemedyCard, SafetyCard
from src.defs.constants import CARD_COUNTS_BY_CARD_TYPE
from src.defs.game import Condition


def create_deck() -> list[Card]:
    cards = []
    for card_type in CARD_COUNTS_BY_CARD_TYPE.keys():
        count = CARD_COUNTS_BY_CARD_TYPE[card_type]
        for _ in range(count):
            cards.append(card_type())

    random.shuffle(cards)
    return cards


def get_top_card(cards: list[Card]) -> Optional[Card]:
    return cards[-1] if len(cards) else None


def safety_card_cures_condition(safety_card: SafetyCard, condition: Condition) -> bool:
    # We have to iterate through all values of the safety card:
    # if it happens to be Right Of Way, it can cure multiple conditions
    return condition in safety_card.value


def find_safety_card_in_hand(hand: list[Card]) -> Optional[Card]:
    return get_top_card([card for card in hand if card.card_type == CardType.safety])


def find_go_card_in_hand(hand: list[Card]) -> Optional[Card]:
    return get_top_card([card for card in hand if card.name == CardName.go])


def find_end_of_limit_card_in_hand(hand: list[Card]) -> Optional[Card]:
    return get_top_card([card for card in hand if card.name == CardName.end_of_limit])


def find_remedy_card_in_hand(hand: list[Card], condition: Condition) -> Optional[Card]:
    return get_top_card(
        [
            card
            for card in hand
            if card.card_type == CardType.remedy and cast(RemedyCard, card).condition == condition
        ]
    )


def find_longest_distance_card_in_hand(
    hand: list[Card], speed_limit: Optional[int]
) -> Optional[Card]:
    distance_cards = [
        cast(DistanceCard, distance_card)
        for distance_card in [card for card in hand if card.card_type == CardType.distance]
    ]
    if speed_limit:
        distance_cards = [card for card in distance_cards if card.value <= speed_limit]
    sorted_cards = sorted(distance_cards, key=lambda card: card.value, reverse=True)
    return sorted_cards[0] if len(sorted_cards) else None


def card_target_is_self(card: Card) -> bool:
    return card.card_type != CardType.hazard
