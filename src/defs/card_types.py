from enum import Enum
from typing import NoReturn, Union, cast

from src.defs.card_names import CardName
from src.defs.game import Condition


class CardType(Enum):
    hazard = "hazard"
    remedy = "remedy"
    safety = "safety"
    distance = "distance"


class Card:
    name: CardName
    card_type: CardType
    value: Union[int, set[Condition]]
    symbol: str = "?"
    description: str = ""


class ConditionCard(Card):
    name: CardName
    card_type: CardType
    value: set[Condition]
    description: str = ""

    @property
    def condition(self) -> Condition:
        # Most condition cards have exactly one condition
        # The only exception is Right of Way; this property
        # will raise an exception if the card is any Safety Card,
        # to make sure we don't try to iterate about the conditions
        # of a list of Safety Cards
        return cast(Condition, list(self.value)[0])


class DistanceCard(Card):
    name: CardName
    card_type: CardType = CardType.distance
    value: int = 0
    description: str = ""


class HazardCard(ConditionCard):
    name: CardName
    card_type: CardType = CardType.hazard
    description: str = ""


class RemedyCard(ConditionCard):
    name: CardName
    card_type: CardType = CardType.remedy
    description: str = ""


class SafetyCard(ConditionCard):
    name: CardName
    card_type: CardType = CardType.safety
    description: str = ""

    @property
    def condition(self) -> NoReturn:
        raise Exception(
            "Unsafe call to 'condition' on SafetyCard: some safety cards have multiple conditions"
        )
