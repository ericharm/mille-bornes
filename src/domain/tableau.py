from collections.abc import Callable

from src.defs.card_names import CardName
from src.defs.card_types import Card, CardType, DistanceCard, HazardCard, RemedyCard
from src.defs.game import Condition
from src.models.tableau import Tableau


def _add_hazard_to_tableau(tableau: Tableau, hazard_card: HazardCard) -> None:
    if hazard_card.condition in tableau.immunities:
        raise Exception("Player has immunity against this hazard")

    if hazard_card.condition == Condition.speed_limit:
        tableau.speed_cards.append(hazard_card)
        return
    tableau.battle_cards.append(hazard_card)


def _add_remedy_to_tableau(tableau: Tableau, remedy_card: RemedyCard) -> None:
    if remedy_card.name == CardName.go:
        if not tableau.can_play_go_card:
            raise Exception("Player cannot play Go card")
        tableau.battle_cards.append(remedy_card)
        return

    if remedy_card.condition not in tableau.active_conditions:
        raise Exception("Player does not have this condition")

    if remedy_card.name == CardName.end_of_limit:
        tableau.speed_cards.append(remedy_card)
        return

    tableau.battle_cards.append(remedy_card)


def _add_distance_card_to_tableau(tableau: Tableau, distance_card: DistanceCard) -> None:
    if not tableau.can_go:
        raise Exception("Player cannot play distance card when Go is not showing")
    if tableau.speed_limit and distance_card.value > tableau.speed_limit:
        raise Exception("Cannot play distance card beyond speed limit")
    tableau.distance_cards.append(distance_card)


CARD_TYPES_TO_TABLEAU_ADDER_FNS: dict[CardType, Callable] = {
    CardType.distance: _add_distance_card_to_tableau,
    CardType.safety: lambda tableau, card: tableau.safety_cards.append(card),
    CardType.hazard: _add_hazard_to_tableau,
    CardType.remedy: _add_remedy_to_tableau,
}


def add_card_to_tableau(tableau: Tableau, card: Card) -> None:
    adder_fn = CARD_TYPES_TO_TABLEAU_ADDER_FNS[card.card_type]
    adder_fn(tableau, card)
