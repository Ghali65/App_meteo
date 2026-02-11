import pandas as pd
import pytest
from p_meteo.modules.transform.t_vent_moyen import TVentMoyen


class DummyRecord:
    pass


@pytest.mark.parametrize(
    "values, expected",
    [
        ([5], 5),
        ([20], 20),
        ([0], 0),
    ]
)
def test_t_vent_moyen(values, expected):
    df = pd.DataFrame({"force_moyenne_du_vecteur_vent": values})
    record = DummyRecord()

    transformer = TVentMoyen()
    result = transformer(df, record)

    assert result.vent_moyen == expected


def test_t_vent_moyen_empty_df(capsys):
    df = pd.DataFrame(columns=["force_moyenne_du_vecteur_vent"])
    record = DummyRecord()

    transformer = TVentMoyen()
    result = transformer(df, record)

    assert result.vent_moyen is None
    assert "DataFrame vide" in capsys.readouterr().out
