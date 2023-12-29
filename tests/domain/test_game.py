import pytest
from unittest.mock import MagicMock, patch
from src.defs.constants import HAND_SIZE, TOTAL_CARD_COUNT
from src.domain.cards import create_deck
from src.domain.game import create_game, deal_cards
from tests.utils.assertions import assert_exception_matches
from tests.utils.game_mocks import deck_factory, game_factory, human_player_factory, player_factory


@patch("src.domain.domain_models.human_player.create_player")
@patch("src.domain.game.create_deck")
def test_create_game(create_deck_mock: MagicMock, create_player_mock: MagicMock) -> None:
    mock_deck = deck_factory()
    create_deck_mock.return_value = mock_deck

    mock_player = human_player_factory()
    create_player_mock.return_value = mock_player

    game = create_game()
    assert game.players == [mock_player]
    assert game.draw_pile == mock_deck.cards
    assert game.discard_pile == []


def test_deal_cards() -> None:
    cards = create_deck()
    player_1 = player_factory()
    game = game_factory(draw_pile=cards, players=[player_1])
    assert len(game.draw_pile) == TOTAL_CARD_COUNT
    assert len(game.players) == 1

    deal_cards(game)

    assert len(game.draw_pile) == TOTAL_CARD_COUNT - HAND_SIZE


def test_deal_cards_already_dealt() -> None:
    game = game_factory(draw_pile=[])
    assert len(game.draw_pile) == 0
    assert len(game.players) == 0

    with pytest.raises(ValueError) as value_error:
        deal_cards(game)

    assert len(game.draw_pile) == 0
    assert_exception_matches(value_error.value, ValueError("Not enough cards in draw pile to deal"))
