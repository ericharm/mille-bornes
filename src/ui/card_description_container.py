from typing import Optional, Union

from textual.reactive import reactive
from textual.widgets import Static

from src.defs.card_types import Card


class CardDescriptionContainer(Static):
    selected_card: Union[reactive, Optional[Card]] = reactive(None)

    def set_selected_card(self, card: Optional[Card]) -> None:
        self.selected_card = card

    def render(self) -> str:
        if self.selected_card is not None:
            return f"{self.selected_card.name.value}:\n{self.selected_card.description}"

        return ""
