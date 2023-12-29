from typing import Optional, cast
from src.defs.card_types import Card, CardType, DistanceCard
from src.defs.constants import SPEED_LIMIT
from src.defs.game import Condition, TableauBase
from src.domain.cards import find_safety_card_in_hand, get_top_card


class PlayerTableau(TableauBase):
    @property
    def top_battle_card(self) -> Optional[Card]:
        # this is probably circular
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

    @property
    def total_distance(self) -> int:
        return sum([cast(DistanceCard, card).value for card in self.distance_cards])

    @property
    def susceptibilities(self) -> list[Condition]:
        # TODO
        return []

    @property
    def is_immune_to_speed_limit(self) -> bool:
        return bool(find_safety_card_in_hand(self.safety_cards, Condition.speed_limit))

    @property
    def is_immune_to_accident(self) -> bool:
        return bool(find_safety_card_in_hand(self.safety_cards, Condition.accident))

    @property
    def is_immune_to_out_of_gas(self) -> bool:
        return bool(find_safety_card_in_hand(self.safety_cards, Condition.out_of_gas))

    @property
    def is_immune_to_flat_tire(self) -> bool:
        return bool(find_safety_card_in_hand(self.safety_cards, Condition.flat_tire))

    @property
    def is_immune_to_stop(self) -> bool:
        return bool(find_safety_card_in_hand(self.safety_cards, Condition.stop))
