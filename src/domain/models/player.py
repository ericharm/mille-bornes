from __future__ import annotations
from abc import ABC
from typing import Optional
from src.defs.card_types import Card
from src.defs.game import Condition, PlayerBase
from src.domain.models.player_tableau import PlayerTableau


class Player(PlayerBase, ABC):
    tableau: PlayerTableau

    def draw_card(self, draw_pile: list[Card]) -> None:
        del draw_pile
        raise NotImplementedError

    def play_card(self, card: Card, player: Player) -> None:
        del card, player
        raise NotImplementedError

    def discard_card(self, discard_pile: list[Card]) -> None:
        del discard_pile
        raise NotImplementedError

    @property
    def speed_limit(self) -> Optional[int]:
        return self.tableau.speed_limit

    @property
    def can_be_targeted_by_hazard(self) -> bool:
        # TODO
        return True

    @property
    def susceptibilities(self) -> list[Condition]:
        # TODO
        return self.tableau.susceptibilities
