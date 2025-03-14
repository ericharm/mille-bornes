from dataclasses import dataclass, field
from typing import Optional, cast

from src.defs.card_types import Card
from src.defs.constants import TARGET_DISTANCE
from src.models.player import Player


@dataclass
class Game:
    players: list[Player]
    draw_pile: list[Card]
    discard_pile: list[Card] = field(default_factory=list)
    current_player_index: int = 0
    turn: int = 0

    @property
    def player_count(self) -> int:
        return len(self.players)

    @property
    def current_player(self) -> Player:
        return cast(Player, self.players[self.current_player_index])

    @property
    def next_player_index(self) -> int:
        next_player_index = self.current_player_index + 1
        if next_player_index >= len(self.players):
            next_player_index = 0
        return next_player_index

    @property
    def next_player(self) -> Player:
        return cast(Player, self.players[self.next_player_index])

    @property
    def victor(self) -> Optional[Player]:
        return next(
            (player for player in self.players if player.distance_traveled >= TARGET_DISTANCE),
            None,
        )
