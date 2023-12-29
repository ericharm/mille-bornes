from enum import Enum


class Condition(Enum):
    accident = "accident"
    out_of_gas = "out_of_gas"
    flat_tire = "flat_tire"
    stop = "stop"
    speed_limit = "speed_limit"


class PlayerType(Enum):
    human = "human"
    computer = "computer"


# class TableauBase(ABC):
#     battle_cards: list[Card]
#     speed_cards: list[Card]
#     distance_cards: list[Card]
#     safety_cards: list[Card]


# class PlayerBase(ABC):
#     name: str
#     player_type: PlayerType
#     tableau: TableauBase
#     hand: list[Card]


# class GameBase(ABC):
#     draw_pile: list[Card]
#     discard_pile: list[Card]
#     players: list[PlayerBase]
#     current_player_index: int = 0
#     turn = 0
