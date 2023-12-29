from defs.constants import HAND_SIZE, TOTAL_CARD_COUNT
from defs.game import Condition
from domain.models.game import Game
from domain.models.player import Player
from src.domain.player import select_playable_card
from src.domain.cards import card_is_played_to_own_tableau, create_deck
from src.domain.models.human_player import HumanPlayer


def create_game() -> Game:
    deck = create_deck()
    player_1 = HumanPlayer()
    return Game(
        # players=[player_1],
        # draw_pile=deck,
        # discard_pile=[],
    )


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

    card = select_playable_card(player=game.current_player)

    if card:
        # TODO select playable card maybe should return the target of hazard cards
        target = game.current_player if card_is_played_to_own_tableau(card) else game.next_player
        game.current_player.play_card(card, target)

    game.current_player.discard_card(game.discard_pile)

    game.current_player_index = game.next_player_index

    return game


def get_player_suscetibilities(players: list[Player]) -> dict[Player, list[Condition]]:
    suscetibilities = {}
    for player in players:
        suscetibilities[player] = player.susceptibilities
    return suscetibilities
