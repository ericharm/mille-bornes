from textual.reactive import reactive
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, Container
from textual.widgets import Header, Footer, Static

from src.defs.ui import STYLESHEET_PATH


class MilleBornesUI(App):
    """
    Terminal UI for Mille Bornes game using Textual.
    """

    CSS_PATH = STYLESHEET_PATH
    TITLE = "Milles-Borne"

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.turn = reactive(game.turn)
        self.card_count = reactive(len(game.draw_pile))

    def compose(self) -> ComposeResult:
        deck_contents = (
            f"🂠 Turn {self.game.turn} | Cards Left: {len(self.game.draw_pile)} "
        )

        yield Header()
        yield Vertical(
            Vertical(
                Horizontal(
                    Static(deck_contents, id="deck"),  # Representing deck
                    id="game_info",
                ),
                *[self.render_player_section(player) for player in self.game.players],
                Static("", id="event_log"),  # Empty event log for now
                id="everything",
            ),
        )
        yield Footer()

    def render_player_section(self, player):
        return Container(
            Horizontal(
                self.get_tableau_display(player),
            ),
            Static(
                self.get_hand_display(player)
                if player == self.game.current_player
                else "",
                id="player_hand",
            ),
            id=f"player_{player.id}",
        )

    def get_tableau_display(self, player):
        return Vertical(
            Static(
                f"{player.name} | "
                f"Battle: {' '.join(c.symbol for c in player.tableau.battle_cards)} | "
                f"Speed: {' '.join(c.symbol for c in player.tableau.speed_cards)} | "
                f"Safety: {' '.join(c.symbol for c in player.tableau.safety_cards)}",
                id="tableau",
            ),
            Static(f"Speed Limit: {player.speed_limit or 'None'}", id="speed_limit"),
            Static(self.get_conditions_display(player), id="conditions"),
            Static(
                f"Distance: {sum(card.value for card in player.tableau.distance_cards)}",
                id="distance",
            ),
            Static(
                "GO" if player.can_go else "STOP",
                id="can_go",
                classes="go" if player.can_go else "stop",
            ),
        )

    def get_conditions_display(self, player):
        return f"Active: {' '.join(cond.value for cond in player.tableau.active_conditions)}"

    def get_hand_display(self, player):
        return "Hand: " + " | ".join(card.symbol for card in player.hand)
