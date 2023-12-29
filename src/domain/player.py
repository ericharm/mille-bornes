from typing import Callable, Optional
from src.defs.cards.cards import Card, CardType
from src.defs.cards.hazards import SpeedLimit
from src.defs.cards.remedies import EndOfLimit, Go, RemedyCard
from src.domain.cards import (
    card_is_go_card,
    card_meets_condition,
    find_end_of_limit_card_in_hand,
    find_go_card_in_hand,
    find_safety_card_in_hand,
)
from src.defs.game import Player, PlayerType, Tableau


def create_tableau() -> Tableau:
    return Tableau(battle_cards=[], speed_cards=[], distance_cards=[], safety_cards=[])


def create_player(player_type: PlayerType, name: str) -> Player:
    return Player(
        name=name,
        player_type=player_type,
        tableau=create_tableau(),
        hand=[],
    )


def player_matches_condition(player: Player, condition: Callable[[Player], bool]) -> bool:
    return condition(player)


def player_can_play_go_card(player: Player) -> bool:
    top_battle_card = player.tableau.top_battle_card

    if not top_battle_card:
        return True

    if card_is_go_card(top_battle_card):
        return False

    # Any remedy card besides Go is okay
    if card_meets_condition(top_battle_card, lambda card: card.card_type == CardType.remedy):
        return True

    return False


def player_can_play_end_of_limit_card(player: Player) -> bool:
    top_speed_card = player.tableau.top_speed_card

    if not top_speed_card:
        return False

    # Can only play End of Limit if the top speed card is a SpeedLimit
    if isinstance(top_speed_card, SpeedLimit):
        return True

    return False


def player_can_play_remedy_card(player: Player, card: RemedyCard) -> bool:
    if isinstance(card, Go):
        return player_can_play_go_card(player)

    if isinstance(card, EndOfLimit):
        return player_can_play_end_of_limit_card(player)

    top_battle_card = player.tableau.top_battle_card
    if not top_battle_card:
        # If the battle pile is empty, you can't play a remedy
        return False

    if top_battle_card.card_type == CardType.hazard and top_battle_card.value == card.value:
        # Remedies can only be played on hazards of the same value
        return True

    return False


def select_playable_card(player: Player) -> Optional[Card]:
    safety_card = find_safety_card_in_hand(player.hand)
    if safety_card:
        return safety_card

    go_card = find_go_card_in_hand(player.hand)
    if go_card and player_can_play_go_card(player):
        return go_card

    other_remedy_cards = [
        card
        for card in player.hand
        if card.card_type == CardType.remedy and not isinstance(card, Go)
        # and it's not a speed limit card?
    ]

    end_of_limit_card = find_end_of_limit_card_in_hand(player.hand)
    if end_of_limit_card and player_can_play_end_of_limit_card(player):
        return end_of_limit_card

    for remedy_card in other_remedy_cards:
        assert isinstance(remedy_card, RemedyCard)
        if player_can_play_remedy_card(player, remedy_card):
            return remedy_card

    # if player has any distance cards larger than their current speed limit,
    # play the largest one

    # if player has any hazard cards
    return None
