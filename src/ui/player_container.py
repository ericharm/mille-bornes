from typing import Any, cast
from textual.app import ComposeResult
from textual.containers import (
    Horizontal,
    Vertical,
)
from textual.widgets import Static

from src.models.player import Player


class TableauContainer(Horizontal):
    def __init__(self, player: Player, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.player = player

    def compose(self) -> ComposeResult:
        conditions = f"Conditions: {' '.join(cond.value for cond in self.player.tableau.active_conditions)}"
        distance = sum(
            cast(int, card.value) for card in self.player.tableau.distance_cards
        )

        yield Vertical(
            Static(self.player.name),
            Static(
                f"Battle: {' '.join(c.symbol for c in self.player.tableau.battle_cards)}"
            ),
            Static(
                f"Speed: {' '.join(c.symbol for c in self.player.tableau.speed_cards)}"
            ),
            Static(
                f"Safety: {' '.join(c.symbol for c in self.player.tableau.safety_cards)}"
            ),
        )

        yield Vertical(
            Static(
                f"Speed Limit: {self.player.speed_limit or 'None'}", id="speed_limit"
            ),
            Static(conditions),
            Static(
                f"Distance: {distance}",
            ),
            Static(
                "GO" if self.player.can_go else "STOP",
            ),
        )


class PlayerContainer(Horizontal):
    def __init__(self, player: Player, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.player = player

    def compose(self) -> ComposeResult:
        yield TableauContainer(self.player)
