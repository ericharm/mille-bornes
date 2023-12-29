from src.defs.constants import TOTAL_CARD_COUNT
from src.domain.cards import create_deck


def test_create_deck() -> None:
    deck = create_deck()
    assert len(deck) == TOTAL_CARD_COUNT
