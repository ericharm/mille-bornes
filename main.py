from src.defs.game import PlayerType
from src.domain import cards as cards_domain
from src.domain import game as game_domain
from src.models.game import Game
from src.models.player import Player

player_1 = Player(name="Player 1", player_type=PlayerType.computer)
player_2 = Player(name="Player 2", player_type=PlayerType.computer)

deck = cards_domain.create_deck()
game = Game(players=[player_1, player_2], draw_pile=deck)
game_domain.deal_cards(game)
