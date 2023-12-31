from dataclasses import dataclass, field
from typing import Optional, cast

from src.defs.card_names import CardName
from src.defs.card_types import Card, CardType, HazardCard, SafetyCard
from src.defs.constants import SPEED_LIMIT
from src.defs.game import Condition
from src.domain.cards import get_top_card


@dataclass
class Tableau:
    battle_cards: list[Card] = field(default_factory=lambda: [])
    speed_cards: list[Card] = field(default_factory=lambda: [])
    distance_cards: list[Card] = field(default_factory=lambda: [])
    safety_cards: list[Card] = field(default_factory=lambda: [])

    @property
    def top_battle_card(self) -> Optional[Card]:
        return get_top_card(self.battle_cards)

    @property
    def top_speed_card(self) -> Optional[Card]:
        return get_top_card(self.speed_cards)

    @property
    def speed_limit(self) -> Optional[int]:
        top_speed_card = self.top_speed_card
        if not top_speed_card:
            return None
        if top_speed_card.card_type == CardType.hazard:
            return SPEED_LIMIT
        return None

    # @property
    # def total_distance(self) -> int:
    #     return sum([cast(DistanceCard, card).value for card in self.distance_cards])

    @property
    def immunities(self) -> list[Condition]:
        immunities = []
        for safety_card in self.safety_cards:
            immunities.extend([condition for condition in cast(SafetyCard, safety_card).value])

        # You're immune to all hazards except speed limits if your battle pile is empty:
        if not self.top_battle_card:
            immunities.extend([Condition.flat_tire, Condition.out_of_gas, Condition.stop])

        # You're immune to speed limits if you already have one:
        if self.speed_limit:
            immunities.append(Condition.speed_limit)

        return immunities

    # @property
    # def susceptibilities(self) -> list[Condition]:
    #     susceptibilities = [condition for condition in Condition]
    #     return [condition for condition in susceptibilities if condition not in self.immunities]

    @property
    def active_conditions(self) -> list[Condition]:
        conditions = []
        top_battle_card = self.top_battle_card

        if not top_battle_card or top_battle_card.name == CardName.go:
            conditions.append(Condition.stop)

        if top_battle_card and top_battle_card.card_type == CardType.hazard:
            conditions.append(cast(HazardCard, top_battle_card).condition)

        top_speed_card = self.top_speed_card

        if top_speed_card and top_speed_card.card_type == CardType.hazard:
            conditions.append(cast(HazardCard, top_speed_card).condition)

        return conditions

    @property
    def can_play_go_card(self) -> bool:
        top_battle_card = self.top_battle_card

        # If the battle pile is empty, you can play a go card
        if not top_battle_card:
            return True

        # If the top battle card is stop, you can play a go card
        if top_battle_card.name == CardName.stop:
            return True

        # If the top battle card is already Go, you can not play a go card
        if top_battle_card.name == CardName.go:
            return False

        # Any remedy card besides Go is okay
        if top_battle_card.card_type == CardType.remedy:
            return True

        return False

    @property
    def can_go(self) -> bool:
        # this is oversimplified, I'm not sure how safety cards factor in
        return bool(self.top_battle_card and self.top_battle_card.name == CardName.go)
