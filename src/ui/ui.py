from typing import Any
from textual.reactive import reactive
from textual.app import App, ComposeResult
from textual.containers import (
    Horizontal,
    Vertical,
    VerticalScroll,
)
from textual.widgets import Header, Static

from src.defs.ui import STYLESHEET_PATH
from src.models.game import Game
from src.models.event_log import EventLog
from src.ui.player_container import PlayerContainer


class EventLogContainer(Horizontal):
    def compose(self) -> ComposeResult:
        yield VerticalScroll(*[Static(message) for message in EventLog.messages])


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
        yield Vertical(
            GameInfo(self.game),
            *[PlayerContainer(player) for player in self.game.players],
            EventLogContainer(),
        )


class MilleBornesUI(App):
    """
    Terminal UI for Mille Bornes game using Textual.
    """

    CSS_PATH = STYLESHEET_PATH
    TITLE = "Milles-Borne"

    def __init__(self, game: Game):
        super().__init__()
        self.game = game
        self.turn = reactive(game.turn)
        self.card_count = reactive(len(game.draw_pile))

    def compose(self) -> ComposeResult:
        yield Header()
        yield GameContainer(self.game)
