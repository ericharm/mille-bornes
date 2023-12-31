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
