from src.defs.card_names import CardName
from src.defs.game import Condition
from src.defs.card_types import DistanceCard, HazardCard, RemedyCard, SafetyCard


class Accident(HazardCard):
    name: CardName = CardName.accident
    value: set[Condition] = {Condition.accident}
    description: str = (
        "When Accident is played, the player must repair the damage before continuing."
    )


class OutOfGas(HazardCard):
    name: CardName = CardName.out_of_gas
    value: set[Condition] = {Condition.out_of_gas}
    description: str = "When Out of Gas is played, the player must get gas before continuing."


class FlatTire(HazardCard):
    name: CardName = CardName.flat_tire
    value: set[Condition] = {Condition.flat_tire}
    description: str = (
        "When Flat flat_tire is played, the player must replace the tire before continuing."
    )


class Stop(HazardCard):
    name: CardName = CardName.stop
    value: set[Condition] = {Condition.stop}
    description: str = (
        "When Stop is played, the player must wait for a green light before continuing."
    )


class SpeedLimit(HazardCard):
    name: CardName = CardName.speed_limit
    value: set[Condition] = {Condition.speed_limit}
    description: str = "The player cannot play a distance card that exceeds the speed_limit limit."


class Repairs(RemedyCard):
    name: CardName = CardName.repairs
    value: set[Condition] = {Condition.accident}
    description: str = "This card can be used to remove an Accident from your battle area."


class Gasoline(RemedyCard):
    name: CardName = CardName.gasoline
    value: set[Condition] = {Condition.out_of_gas}
    description: str = "This card can be used to remove an Out of Gas from your battle area."


class SpareTire(RemedyCard):
    name: CardName = CardName.spare_tire
    value: set[Condition] = {Condition.flat_tire}
    description: str = "This card can be used to remove a Flat flat_tire from your battle area."


class Go(RemedyCard):
    name: CardName = CardName.go
    value: set[Condition] = {Condition.stop}
    description: str = "This card can be used to remove a Stop from your battle area."


class EndOfLimit(RemedyCard):
    name: CardName = CardName.end_of_limit
    value: set[Condition] = {Condition.speed_limit}
    description: str = "This card can be used to remove speed_limit Limit from your battle area."


class Distance25(DistanceCard):
    name: CardName = CardName.distance_25
    value = 25
    description = "Progress the player 25 miles along the raceway."


class Distance50(DistanceCard):
    name: CardName = CardName.distance_50
    value = 50
    description = "Progress the player 50 miles along the raceway."


class Distance75(DistanceCard):
    name: CardName = CardName.distance_75
    value = 75
    description = "Progress the player 75 miles along the raceway."


class Distance100(DistanceCard):
    name = CardName.distance_100
    value = 100
    description = "Progress the player 100 miles along the raceway."


class Distance200(DistanceCard):
    name = CardName.distance_200
    value = 200
    description = "Progress the player 200 miles along the raceway."


class DrivingAce(SafetyCard):
    name: CardName = CardName.driving_ace
    value: set[Condition] = {Condition.accident}
    description: str = "This card protects the player from Accidents."


class ExtraTank(SafetyCard):
    name: CardName = CardName.extra_tank
    value: set[Condition] = {Condition.out_of_gas}
    description: str = "This card protects the player from Out of Gas."


class PunctureProof(SafetyCard):
    name: CardName = CardName.puncture_proof
    value: set[Condition] = {Condition.flat_tire}
    description: str = "This card protects the player from Flat flat_tire."


class RightOfWay(SafetyCard):
    name: CardName = CardName.right_of_way
    value: set[Condition] = {Condition.stop, Condition.speed_limit}
    description: str = "This card protects the player from Stop and speed_limit Limit."
