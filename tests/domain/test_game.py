import pytest
from src.defs.card_names import CardName
from src.defs.constants import HAND_SIZE, TOTAL_CARD_COUNT
from src.defs import cards
from src.domain.cards import create_deck, find_longest_distance_card_in_hand
from src.domain.game import deal_cards, play_game_turn
from src.models.computer_player import ComputerPlayer
from src.models.game import Game
from tests.utils.assertions import assert_exception_matches


def _generate_game() -> Game:
    cards = create_deck()
    player_1 = ComputerPlayer(name="Player 1")
    player_2 = ComputerPlayer(name="Player 2")
    return Game(draw_pile=cards, players=[player_1, player_2])


def test_deal_cards() -> None:
    game = _generate_game()
    player_1, player_2 = game.players

    assert len(game.draw_pile) == TOTAL_CARD_COUNT
    assert len(game.players) == 2
    assert len(player_1.hand) == 0
    assert len(player_2.hand) == 0

    deal_cards(game)

    assert len(game.draw_pile) == TOTAL_CARD_COUNT - (HAND_SIZE * 2)
    assert len(player_1.hand) == HAND_SIZE
    assert len(player_2.hand) == HAND_SIZE


def test_deal_cards_already_dealt() -> None:
    player_1 = ComputerPlayer(name="Player 1")
    game = Game(players=[player_1], draw_pile=[])
    assert len(game.players) == 1
    assert len(game.players[0].hand) == 0
    assert len(game.draw_pile) == 0

    with pytest.raises(ValueError) as value_error:
        deal_cards(game)

    assert len(game.players[0].hand) == 0
    assert len(game.draw_pile) == 0
    assert_exception_matches(value_error.value, ValueError("Not enough cards in draw pile to deal"))


def test_play_game_turn_a_play_is_selected() -> None:
    game = _generate_game()

    deal_cards(game)

    # We'll set Player 1's hand to something that makes their first move
    # very predictable
    player_1, player_2 = game.players
    player_1.hand = [
        cards.Go(),
        cards.Go(),
        cards.Go(),
        cards.Go(),
        cards.Go(),
        cards.Go(),
    ]

    # And put a useless card at the top of the draw pile so we know it won't
    # be selected
    distance_card = find_longest_distance_card_in_hand(game.draw_pile, None)
    assert distance_card
    game.draw_pile.remove(distance_card)
    game.draw_pile.append(distance_card)

    assert game.turn == 0
    assert player_1.tableau.battle_cards == []
    assert len(player_1.hand) == HAND_SIZE
    assert game.current_player == player_1
    assert len(game.draw_pile) == TOTAL_CARD_COUNT - (HAND_SIZE * 2)
    assert len(game.discard_pile) == 0

    play_game_turn(game)

    # Now it's turn 1
    assert game.turn == 1
    assert len(player_1.tableau.battle_cards) == 1
    assert player_1.tableau.top_battle_card
    # Player 1 played a Go card
    assert player_1.tableau.top_battle_card.name == CardName.go
    # Player 1 still has 6 cards, they did not discard
    assert len(player_1.hand) == HAND_SIZE
    # The game's draw pile has decreased by 1
    assert len(game.draw_pile) == TOTAL_CARD_COUNT - (HAND_SIZE * 2) - 1
    assert len(game.discard_pile) == 0

    # Now it's Player 2's turn
    assert game.current_player == player_2


def test_play_game_turn_no_play_available() -> None:
    game = _generate_game()

    deal_cards(game)

    # We'll give Player 1 a bunch of cards they can't play,
    # since they don't have a Go card in their battle pile to start
    player_1, player_2 = game.players
    player_1.hand = [
        cards.Distance25(),
        cards.Distance25(),
        cards.Distance25(),
        cards.Distance25(),
        cards.Distance25(),
        cards.Distance25(),
    ]

    assert game.turn == 0
    assert player_1.tableau.battle_cards == []
    assert len(player_1.hand) == HAND_SIZE
    assert game.current_player == player_1
    assert len(game.draw_pile) == TOTAL_CARD_COUNT - (HAND_SIZE * 2)
    assert len(game.discard_pile) == 0

    # Put another useless card at the top of the draw pile
    distance_card = find_longest_distance_card_in_hand(game.draw_pile, None)
    assert distance_card
    game.draw_pile.remove(distance_card)
    game.draw_pile.append(distance_card)

    play_game_turn(game)

    # Now it's turn 1
    assert game.turn == 1
    # Player 1 wasn't able to play anything
    assert player_1.tableau.battle_cards == []
    assert player_1.tableau.speed_cards == []
    assert player_1.tableau.distance_cards == []
    assert player_1.tableau.safety_cards == []
    # Player 1 still has 6 cards, they did discarded the drawn card
    assert len(player_1.hand) == HAND_SIZE
    # A card was removed from the draw pile
    assert len(game.draw_pile) == TOTAL_CARD_COUNT - (HAND_SIZE * 2) - 1
    # A card was added to the discard pile
    assert len(game.discard_pile) == 1

    # Now it's Player 2's turn
    assert game.current_player == player_2


def test_play_game_turn_for_player_2() -> None:
    # Will need to test this to get 100% coverage
    pass
