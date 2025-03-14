from typing import Any

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.message import Message
from textual.widgets import Button, Static

from src.defs.card_types import Card
from src.models.player import Player


class CardButton(Button):
    """A button representing a Mille Bornes card."""

    def __init__(self, card: Card, **kwargs: Any) -> None:
        super().__init__(card.symbol, **kwargs)  # Display the card's symbol as the button text
        self.card = card

    class CardSelected(Message):
        """Event emitted when a card is selected."""

        def __init__(self, card: Card) -> None:
            super().__init__()
            self.card = card  # Store selected card

    def on_click(self) -> None:
        """Handle button click and notify the app."""
        self.post_message(self.CardSelected(self.card))


class HandContainer(Static):
    def __init__(self, player: Player, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.player = player

    def compose(self) -> ComposeResult:
        yield Vertical(
            Static("Hand:"),
            Static(""),
            Horizontal(*[CardButton(card) for card in self.player.hand]),
        )
