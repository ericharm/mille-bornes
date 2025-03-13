from src.defs.constants import HAND_SIZE, TOTAL_CARD_COUNT
from src.models.game import Game


def deal_cards(game: Game) -> Game:
    if len(game.draw_pile) < TOTAL_CARD_COUNT:
        raise ValueError("Not enough cards in draw pile to deal")

    for player in game.players:
        while len(player.hand) < HAND_SIZE:
            player.hand.append(game.draw_pile.pop())

    return game


def play_game_turn(game: Game) -> Game:
    if game.current_player_index == 0:
        game.turn += 1

    game.current_player.draw_card(game.draw_pile)
    play = game.current_player.select_playable_card()

    if play:
        game.current_player.play_card(play.card, play.target)

    game.current_player.discard_card(game.discard_pile)
    game.current_player_index = game.next_player_index

    return game
