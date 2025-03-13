from __future__ import annotations

import uuid
from abc import ABC
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional, cast

from src.defs.card_types import Card, CardType, HazardCard
from src.defs.constants import HAND_SIZE
from src.defs.game import Condition
from src.defs.player import Play, PlayerBase, PlayerType
from src.domain.tableau import add_card_to_tableau
from src.models.event_log import EventLog
from src.models.tableau import Tableau


@dataclass
class Player(PlayerBase, ABC):
    name: str
    player_type: PlayerType
    tableau: Tableau = field(default_factory=lambda: Tableau())
    hand: list[Card] = field(default_factory=list)

    def draw_card(self, draw_pile: list[Card]) -> None:
        self.hand.append(draw_pile.pop())

    def play_card(self, card: Card, target: Optional[PlayerBase] = None) -> None:
        self.hand.remove(card)
        add_card_to_tableau(self.tableau if not target else target.tableau, card)
        EventLog.append_message(f"{self.name} played {card.name.value}")

    def discard_card(self, discard_pile: list) -> None:
        if len(self.hand) > HAND_SIZE:
            # TODO: we should devise an algorithm for determining
            # the strength of each card in the player's hand based
            # on the tableau
            # A very simple approach would be to provide an attribute on each card
            # inidicating its relative strength
            discard_pile.append(self.hand.pop())

    def select_playable_card(self) -> Optional[Play]:
        raise NotImplementedError

    @property
    def can_go(self) -> bool:
        return self.tableau.can_go

    @property
    def can_play_go_card(self) -> bool:
        return self.tableau.can_play_go_card

    @property
    def speed_limit(self) -> Optional[int]:
        return self.tableau.speed_limit

    @property
    def battle_hazard(self) -> Optional[Condition]:
        top_battle_card = self.tableau.top_battle_card
        if not top_battle_card:
            return None
        if top_battle_card.card_type != CardType.hazard:
            return None
        hazard_card = cast(HazardCard, top_battle_card)
        hazard, *_ = [condition for condition in hazard_card.value]
        return hazard

    @cached_property
    def id(self) -> str:
        return str(uuid.uuid4())
