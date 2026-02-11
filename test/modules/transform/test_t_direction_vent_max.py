import pandas as pd
import pytest
from p_meteo.modules.transform.t_direction_vent_max import TDirectionVentMax


class DummyRecord:
    pass


@pytest.mark.parametrize(
    "values, expected",
    [
        ([0], 0),
        ([270], 270),
        ([359], 359),
    ]
)
def test_t_direction_vent_max(values, expected):
    df = pd.DataFrame({
        "direction_du_vecteur_de_vent_max": values
    })
    record = DummyRecord()

    transformer = TDirectionVentMax()
    result = transformer(df, record)

    assert result.direction_vent_max == expected


def test_t_direction_vent_max_empty_df(capsys):
    df = pd.DataFrame(columns=["direction_du_vecteur_de_vent_max"])
    record = DummyRecord()

    transformer = TDirectionVentMax()
    result = transformer(df, record)

    assert result.direction_vent_max is None
    assert "DataFrame vide" in capsys.readouterr().out
