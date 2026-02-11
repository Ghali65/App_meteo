import pandas as pd
import pytest
from p_meteo.modules.transform.t_direction_vent_max_deg import TDirectionVentMaxDeg


class DummyRecord:
    pass


@pytest.mark.parametrize(
    "values, expected",
    [
        ([120], 120),
        ([45], 45),
        ([10], 10),
    ]
)
def test_t_direction_vent_max_deg(values, expected):
    df = pd.DataFrame({
        "direction_du_vecteur_de_vent_max_en_degres": values
    })
    record = DummyRecord()

    transformer = TDirectionVentMaxDeg()
    result = transformer(df, record)

    assert result.direction_vent_max_deg == expected


def test_t_direction_vent_max_deg_empty_df(capsys):
    df = pd.DataFrame(columns=["direction_du_vecteur_de_vent_max_en_degres"])
    record = DummyRecord()

    transformer = TDirectionVentMaxDeg()
    result = transformer(df, record)

    assert result.direction_vent_max_deg is None
    assert "DataFrame vide" in capsys.readouterr().out
