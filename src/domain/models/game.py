from typing import cast
from defs.card_types import Card
from domain.models.player import Player
from src.defs.game import GameBase


class Game(GameBase):
    # draw_pile: list[Card]
    # discard_pile: list[Card]
    # players: list[Player]
    # current_player_index: int = 0
    # turn = 0

    def __init__(
        self, draw_pile: list[Card], discard_pile: list[Card], players: list[Player]
    ) -> None:
        super().__init__(draw_pile=draw_pile, discard_pile=discard_pile, players=players)

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
