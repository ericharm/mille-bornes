from textual import on
from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header

from src.defs.ui import STYLESHEET_PATH
from src.domain.game import play_game_turn
from src.models.game import Game
from src.ui.card_description_container import CardDescriptionContainer
from src.ui.event_log_container import EventLogContainer
from src.ui.game_container import GameContainer, NextButton
from src.ui.hand_container import CardButton


class MilleBornesUI(App):
    CSS_PATH = STYLESHEET_PATH
    TITLE = "Mille Bornes"

    def __init__(self, game: Game):
        super().__init__()
        self.game = game

    def on_card_button_card_selected(self, event: CardButton.CardSelected) -> None:
        self.query_one(CardDescriptionContainer).set_selected_card(event.card)

    @on(NextButton.NextPressed)
    async def on_next_button_pressed(self, event: NextButton.NextPressed) -> None:
        event.prevent_default()
        play_game_turn(self.game)
        await self.query_one(GameContainer).recompose()
        await self.query_one(EventLogContainer).recompose()

    def compose(self) -> ComposeResult:
        yield Header()
        yield GameContainer(self.game)
        yield Vertical(
            CardDescriptionContainer(),
            EventLogContainer(id="right"),
        )
