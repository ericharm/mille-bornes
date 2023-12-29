from typing import Any
from src.domain.domain_models.human_player import HumanPlayer
from src.defs.cards.cards import Deck
from src.defs.game import Game, Player, PlayerType, Tableau


def deck_factory() -> Deck:
    deck = Deck(cards=[])
    return deck


def player_factory() -> Player:
    player = Player(
        name="Player 1",
        player_type=PlayerType.human,
        tableau=Tableau(
            battle_cards=[],
            speed_cards=[],
            distance_cards=[],
            safety_cards=[],
        ),
        hand=[],
    )
    return player


def human_player_factory() -> HumanPlayer:
    player = player_factory()
    return HumanPlayer(
        name=player.name,
    )


def game_factory(**kwargs: Any) -> Game:
    game = Game(
        draw_pile=[],
        discard_pile=[],
        players=[],
    )
    for key, value in kwargs.items():
        setattr(game, key, value)
    return game
