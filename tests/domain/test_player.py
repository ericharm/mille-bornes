from unittest.mock import patch, MagicMock
from src.defs.game import PlayerType, Tableau
from src.domain.player import create_player, create_tableau


@patch("src.domain.player.create_tableau")
def test_create_player(create_table_mock: MagicMock) -> None:
    create_table_mock.return_value = Tableau(
        battle_cards=[],
        distance_cards=[],
        speed_cards=[],
        safety_cards=[],
    )

    player = create_player(player_type=PlayerType.human, name="Player 1")
    assert player.name == "Player 1"
    assert player.player_type == PlayerType.human
    assert player.tableau.battle_cards == []
    assert player.tableau.speed_cards == []
    assert player.tableau.distance_cards == []
    assert player.tableau.safety_cards == []
    assert player.hand == []
    create_table_mock.assert_called_once()


def test_create_tableau() -> None:
    tableau = create_tableau()
    assert tableau.battle_cards == []
    assert tableau.speed_cards == []
    assert tableau.distance_cards == []
    assert tableau.safety_cards == []
