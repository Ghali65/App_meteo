import pandas as pd
import pytest
from p_meteo.modules.transform.t_direction_vent_moyen import TDirectionVentMoyen


class DummyRecord:
    pass


@pytest.mark.parametrize(
    "values, expected",
    [
        ([315], 315),
        ([0], 0),
        ([270], 270),
    ]
)
def test_t_direction_vent_moyen(values, expected):
    df = pd.DataFrame({
        "direction_du_vecteur_vent_moyen": values
    })
    record = DummyRecord()

    transformer = TDirectionVentMoyen()
    result = transformer(df, record)

    assert result.direction_vent_moyen == expected


def test_t_direction_vent_moyen_empty_df(capsys):
    df = pd.DataFrame(columns=["direction_du_vecteur_vent_moyen"])
    record = DummyRecord()

    transformer = TDirectionVentMoyen()
    result = transformer(df, record)

    assert result.direction_vent_moyen is None
    assert "DataFrame vide" in capsys.readouterr().out
