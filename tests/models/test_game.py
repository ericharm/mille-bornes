from src.domain import cards as cards_domain
from src.models.computer_player import ComputerPlayer
from src.models.game import Game


def test_game() -> None:
    player_1 = ComputerPlayer(name="Player 1")
    player_2 = ComputerPlayer(name="Player 2")

    deck = cards_domain.create_deck()
    game = Game(players=[player_1, player_2], draw_pile=deck)

    assert game.player_count == 2
    assert game.current_player == player_1
    assert game.next_player == player_2
    assert game.draw_pile == deck
