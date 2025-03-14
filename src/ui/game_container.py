from typing import Any
from textual.app import ComposeResult
from textual.containers import (
    Horizontal,
    Vertical,
)
from textual.widgets import Static

from src.models.game import Game
from src.ui.hand_container import HandContainer
from src.ui.player_container import PlayerContainer


class GameInfo(Horizontal):
    def __init__(self, game, **kwargs) -> None:
        super().__init__(**kwargs)
        self.game = game

    def compose(self) -> ComposeResult:
        yield Static(
            f"🂠 Turn {self.game.turn} | Cards Left: {len(self.game.draw_pile)} "
        )


class GameContainer(Vertical):
    def __init__(self, game: Game, **kwargs: Any):
        super().__init__(**kwargs)
        self.game = game

    def compose(self) -> ComposeResult:
        yield GameInfo(self.game)
        for player in self.game.players:
            yield PlayerContainer(player)
        yield HandContainer(self.game.players[0])
