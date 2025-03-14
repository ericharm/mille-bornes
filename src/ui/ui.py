from typing import Optional
from textual import on
from textual.containers import Vertical
from textual.reactive import reactive
from textual.app import App, ComposeResult
from textual.widgets import Header

from src.defs.ui import STYLESHEET_PATH
from src.models.game import Game
from src.ui.card_description_container import CardDescriptionContainer
from src.ui.event_log_container import EventLogContainer
from src.ui.game_container import GameContainer
from src.ui.hand_container import CardButton


class MilleBornesUI(App):
    """
    Terminal UI for Mille Bornes game using Textual.
    """

    CSS_PATH = STYLESHEET_PATH
    TITLE = "Mille Borne"

    def __init__(self, game: Game):
        super().__init__()
        self.game = game
        self.turn = reactive(game.turn)
        self.card_count = reactive(len(game.draw_pile))

    @on(CardButton.CardSelected)
    def on_card_button_card_selected(self, event: CardButton.CardSelected) -> None:
        self.query_one(CardDescriptionContainer).set_selected_card(event.card)

    def compose(self) -> ComposeResult:
        yield Header()
        yield GameContainer(self.game)
        yield Vertical(
            CardDescriptionContainer(),
            EventLogContainer(id="right"),
        )
