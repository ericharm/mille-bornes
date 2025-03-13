from src.ui.ui import MilleBornesUI


if __name__ == "__main__":
    from src.models.computer_player import ComputerPlayer
    from src.domain import cards as cards_domain
    from src.domain import game as game_domain
    from src.models.game import Game

    player_1 = ComputerPlayer(name="Player 1")
    player_2 = ComputerPlayer(name="Player 2")

    deck = cards_domain.create_deck()
    game = Game(players=[player_1, player_2], draw_pile=deck)
    game_domain.deal_cards(game)
    game_domain.play_game_turn(game)
    MilleBornesUI(game).run()
