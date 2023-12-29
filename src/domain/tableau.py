from typing import cast
from src.defs.cards.hazards import HazardCard
from src.defs.cards.remedies import RemedyCard
from src.domain.cards import card_meets_condition, get_top_card, remedy_card_cures_hazard_card
from src.defs.cards.cards import Card, CardType, Concern
from src.defs.game import Tableau


def add_card_to_tableau(tableau: Tableau, card: Card) -> None:
    if card.card_type == CardType.safety:
        tableau.safety_cards.append(card)
    if card.card_type == CardType.remedy:
        assert isinstance(card, RemedyCard)
        add_remedy_to_tableu(tableau, card)
    if card.card_type == CardType.hazard:
        assert isinstance(card, HazardCard)
        add_hazard_to_tableu(tableau, card)
    if card.card_type == CardType.distance:
        tableau.distance_cards.append(card)


def add_hazard_to_tableu(tableau: Tableau, hazard: HazardCard) -> None:
    card = cast(Card, hazard)
    if hazard.value == Concern.speed:
        top_speed_card = get_top_card(tableau.speed_cards)

        if top_speed_card and card_meets_condition(
            top_speed_card,
            lambda card: card.card_type == CardType.hazard and card.value == Concern.speed,
        ):
            raise Exception("Cannot add a second speed limit card to the speed stack")

        add_card_to_tableau(tableau, card)

    else:
        top_battle_card = get_top_card(tableau.battle_cards)
        if top_battle_card and card_meets_condition(
            card=top_battle_card, condition=lambda card: card.card_type == CardType.hazard
        ):
            raise Exception("Cannot add a second hazard card to the battle stack")

        add_card_to_tableau(tableau, card)


def add_remedy_to_tableu(tableau: Tableau, remedy: RemedyCard) -> None:
    card = cast(Card, remedy)
    if remedy.value == Concern.speed:
        top_speed_card = get_top_card(tableau.speed_cards)
        if top_speed_card and not card_meets_condition(
            card=top_speed_card,
            condition=lambda card: card.card_type == CardType.hazard
            and Card.value == Concern.speed,
        ):
            raise Exception("No speed limit to remove")

        add_card_to_tableau(tableau, card)
    else:
        top_battle_card = get_top_card(tableau.battle_cards)
        if top_battle_card and not card_meets_condition(
            card=top_battle_card,
            condition=lambda card: remedy_card_cures_hazard_card(remedy, card),
        ):
            raise Exception("No hazard to remove")

        add_card_to_tableau(tableau, card)
