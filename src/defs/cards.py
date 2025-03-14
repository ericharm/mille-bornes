from src.defs.card_names import CardName
from src.defs.card_types import DistanceCard, HazardCard, RemedyCard, SafetyCard
from src.defs.game import Condition


class Accident(HazardCard):
    name: CardName = CardName.accident
    value: set[Condition] = {Condition.accident}
    symbol: str = "X"
    description: str = (
        "When Accident is played, the player must repair the damage before continuing."
    )


class OutOfGas(HazardCard):
    name: CardName = CardName.out_of_gas
    value: set[Condition] = {Condition.out_of_gas}
    symbol: str = "G"
    description: str = "When Out of Gas is played, the player must get gas before continuing."


class FlatTire(HazardCard):
    name: CardName = CardName.flat_tire
    value: set[Condition] = {Condition.flat_tire}
    symbol: str = "T"
    description: str = (
        "When Flat Tire is played, the player must replace the tire before continuing."
    )


class Stop(HazardCard):
    name: CardName = CardName.stop
    value: set[Condition] = {Condition.stop}
    symbol = "🛑"
    description: str = (
        "When Stop is played, the player must wait for a green light before continuing."
    )


class SpeedLimit(HazardCard):
    name: CardName = CardName.speed_limit
    value: set[Condition] = {Condition.speed_limit}
    symbol = "S"
    description: str = "The player cannot play a distance card that exceeds the Speed Limit."


class Repairs(RemedyCard):
    name: CardName = CardName.repairs
    value: set[Condition] = {Condition.accident}
    symbol = "x"
    description: str = "This card can be used to remove an Accident from your battle area."


class Gasoline(RemedyCard):
    name: CardName = CardName.gasoline
    value: set[Condition] = {Condition.out_of_gas}
    symbol = "g"
    description: str = "This card can be used to remove an Out of Gas from your battle area."


class SpareTire(RemedyCard):
    name: CardName = CardName.spare_tire
    value: set[Condition] = {Condition.flat_tire}
    symbol = "t"
    description: str = "This card can be used to remove a Flat Tire from your battle area."


class Go(RemedyCard):
    name: CardName = CardName.go
    value: set[Condition] = {Condition.stop}
    symbol = "🟢"
    description: str = "Play this card to permit playing distance cards."


class EndOfLimit(RemedyCard):
    name: CardName = CardName.end_of_limit
    value: set[Condition] = {Condition.speed_limit}
    symbol = "s"
    description: str = "This card can be used to remove Speed Limit from your battle area."


class Distance25(DistanceCard):
    name: CardName = CardName.distance_25
    value = 25
    symbol = "25"
    description = "Progress the player 25 miles along the raceway."


class Distance50(DistanceCard):
    name: CardName = CardName.distance_50
    value = 50
    symbol = "50"
    description = "Progress the player 50 miles along the raceway."


class Distance75(DistanceCard):
    name: CardName = CardName.distance_75
    value = 75
    symbol = "75"
    description = "Progress the player 75 miles along the raceway."


class Distance100(DistanceCard):
    name = CardName.distance_100
    value = 100
    symbol = "100"
    description = "Progress the player 100 miles along the raceway."


class Distance200(DistanceCard):
    name = CardName.distance_200
    value = 200
    symbol = "200"
    description = "Progress the player 200 miles along the raceway."


class DrivingAce(SafetyCard):
    name: CardName = CardName.driving_ace
    value: set[Condition] = {Condition.accident}
    symbol: str = "🏎️"
    description: str = "This card protects the player from Accidents."


class ExtraTank(SafetyCard):
    name: CardName = CardName.extra_tank
    value: set[Condition] = {Condition.out_of_gas}
    symbol: str = "⛽"
    description: str = "This card protects the player from Out of Gas."


class PunctureProof(SafetyCard):
    name: CardName = CardName.puncture_proof
    value: set[Condition] = {Condition.flat_tire}
    symbol: str = "🔧"
    description: str = "This card protects the player from Flat Tire."


class RightOfWay(SafetyCard):
    name: CardName = CardName.right_of_way
    value: set[Condition] = {Condition.stop, Condition.speed_limit}
    symbol: str = "🚦"
    description: str = "This card protects the player from Stop and Speed Limit."
