from src.defs.constants import HAND_SIZE, TOTAL_CARD_COUNT
from src.domain.cards import card_target_is_self
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

    card = game.current_player.select_playable_card()

    if card:
        # TODO select playable card maybe should return the target of hazard cards
        target = game.current_player if card_target_is_self(card) else game.next_player
        game.current_player.play_card(card, target)

    game.current_player.discard_card(game.discard_pile)

    game.current_player_index = game.next_player_index

    return game
