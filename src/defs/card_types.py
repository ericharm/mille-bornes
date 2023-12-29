from enum import Enum
from typing import Optional, Union
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
    description: Optional[str] = None


class ConditionCard:
    name: CardName
    card_type: CardType
    value: set[Condition]
    description: Optional[str] = None


class DistanceCard:
    name: CardName
    card_type: CardType = CardType.distance
    value: int = 0
    description: Optional[str] = None


class HazardCard(ConditionCard):
    name: CardName
    card_type: CardType = CardType.hazard
    description: Optional[str] = None


class RemedyCard(ConditionCard):
    name: CardName
    card_type: CardType = CardType.remedy
    description: Optional[str] = None


class SafetyCard(ConditionCard):
    name: CardName
    card_type: CardType = CardType.safety
    description: Optional[str] = None
