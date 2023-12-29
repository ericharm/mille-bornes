from src.defs.card_types import Card
from src.domain.models.player import Player
from src.domain.tableau import add_card_to_tableau
from src.defs.constants import HAND_SIZE


class HumanPlayer(Player):
    def draw_card(self, draw_pile: list) -> None:
        self.hand.append(draw_pile.pop())

    def play_card(self, card: Card, target: Player) -> None:
        self.hand.remove(card)
        add_card_to_tableau(target.tableau, card)

    def discard_card(self, discard_pile: list) -> None:
        if len(self.hand) > HAND_SIZE:
            discard_pile.append(self.hand.pop())

    def _add_card_to_tableau(self, card: Card) -> None:
        add_card_to_tableau(self.tableau, card)
