from src.defs.constants import HAND_SIZE, TOTAL_CARD_COUNT
from src.domain.cards import create_deck
from src.domain.game import deal_cards
from src.models.computer_player import ComputerPlayer
from src.models.game import Game


def test_deal_cards() -> None:
    cards = create_deck()
    player_1 = ComputerPlayer(name="Player 1")
    player_2 = ComputerPlayer(name="Player 2")

    game = Game(draw_pile=cards, players=[player_1, player_2])

    assert len(game.draw_pile) == TOTAL_CARD_COUNT
    assert len(game.players) == 2
    assert len(player_1.hand) == 0
    assert len(player_2.hand) == 0

    deal_cards(game)

    assert len(game.draw_pile) == TOTAL_CARD_COUNT - (HAND_SIZE * 2)
    assert len(player_1.hand) == HAND_SIZE
    assert len(player_2.hand) == HAND_SIZE


# def test_deal_cards_already_dealt() -> None:
#     game = game_factory(draw_pile=[])
#     assert len(game.draw_pile) == 0
#     assert len(game.players) == 0

#     with pytest.raises(ValueError) as value_error:
#         deal_cards(game)

#     assert len(game.draw_pile) == 0
#     assert_exception_matches(value_error.value,
#  ValueError("Not enough cards in draw pile to deal"))
