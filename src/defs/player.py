from abc import ABC
from dataclasses import dataclass
from enum import Enum
from typing import Optional

from src.defs.card_types import Card
from src.models.tableau import Tableau


class PlayerType(str, Enum):
    human = "human"
    computer = "computer"


@dataclass
class PlayerBase(ABC):
    name: str
    player_type: PlayerType
    tableau: Tableau
    hand: list[Card]


@dataclass
class Play:
    card: Card
    target: Optional[PlayerBase]
