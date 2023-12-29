from enum import Enum


class CardName(Enum):
    # Hazard Cards
    accident = "Accident"
    flat_tire = "Flat Tire"
    out_of_gas = "Out Of Gas"
    stop = "Stop"
    speed_limit = "Speed Limit"
    # Remedy Cards
    repairs = "Repairs"
    gasoline = "Gasoline"
    spare_tire = "Spare Tire"
    go = "Go"
    end_of_limit = "End of Limit"
    # Safety Cards
    driving_ace = "Driving Ace"
    extra_tank = "Extra Tank"
    puncture_proof = "Puncture Proof"
    right_of_way = "Emergency Vehicle / Right of Way"
    # Distance Cards
    distance_25 = "25"
    distance_50 = "50"
    distance_75 = "75"
    distance_100 = "100"
    distance_200 = "200"
