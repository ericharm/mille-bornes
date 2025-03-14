from typing import Optional

from src.defs.player import Play, PlayerType
from src.domain.cards import (
    find_end_of_limit_card_in_hand,
    find_go_card_in_hand,
    find_longest_distance_card_in_hand,
    find_remedy_card_in_hand,
    find_safety_card_in_hand,
)
from src.models.player import Player


class ComputerPlayer(Player):
    def __init__(self, name: str) -> None:
        super().__init__(name=name, player_type=PlayerType.computer)

    def select_playable_card(self) -> Optional[Play]:
        # Play a safety card if you have one, you get to go again anyway
        safety_card = find_safety_card_in_hand(self.hand)
        if safety_card:
            return Play(safety_card, self)

        # TODO: make sure the player actually does take another turn after playing
        # a safety card

        # Remedy any hazards at the top of your battle pile
        battle_hazard = self.battle_hazard
        if battle_hazard:
            remedy_card = find_remedy_card_in_hand(self.hand, battle_hazard)
            if remedy_card:
                return Play(remedy_card, self)

        # Play Go if you have it and are not burdened by any hazards
        go_card = find_go_card_in_hand(self.hand)
        if go_card and self.can_play_go_card:
            return Play(go_card, self)

        # Try to play a distance card
        if self.can_go:
            longest_distance_card = find_longest_distance_card_in_hand(self.hand, self.speed_limit)
            if longest_distance_card:
                return Play(longest_distance_card, self)

        if self.speed_limit:
            end_of_limit_card = find_end_of_limit_card_in_hand(self.hand)
            if end_of_limit_card:
                return Play(end_of_limit_card, self)

        # TODO: try to play a hazard card (for now selfs will just be really nice)
        return None
