from typing import Type
from src.defs import cards

SPEED_LIMIT = 50

HAND_SIZE = 6

CARD_COUNTS_BY_CARD_TYPE: dict[Type, int] = {
    cards.Accident: 3,
    cards.OutOfGas: 3,
    cards.FlatTire: 3,
    cards.Stop: 5,
    cards.SpeedLimit: 4,
    cards.Repairs: 6,
    cards.Gasoline: 6,
    cards.SpareTire: 6,
    cards.Go: 14,
    cards.EndOfLimit: 6,
    cards.DrivingAce: 1,
    cards.ExtraTank: 1,
    cards.PunctureProof: 1,
    cards.RightOfWay: 1,
    cards.Distance25: 10,
    cards.Distance50: 10,
    cards.Distance75: 10,
    cards.Distance100: 12,
    cards.Distance200: 4,
}

TOTAL_CARD_COUNT = sum(CARD_COUNTS_BY_CARD_TYPE.values())
