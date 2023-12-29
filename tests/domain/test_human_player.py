from src.domain.cards import create_deck
from tests.utils.game_mocks import human_player_factory


def test_draw_card() -> None:
    human_player = human_player_factory()
    deck = create_deck()

    hand_size = len(human_player.hand)
    deck_size = len(deck)

    human_player.draw_card(deck)

    assert len(human_player.hand) == hand_size + 1
    assert len(deck) == deck_size - 1


def test_play_card() -> None:
    pass


def test_discard_card() -> None:
    pass
