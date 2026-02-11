import pandas as pd
import pytest
from p_meteo.modules.transform.t_ville import TVille


class DummyRecord:
    pass


@pytest.mark.parametrize(
    "values, expected",
    [
        (["Paris"], "Paris"),
        (["Toulouse"], "Toulouse"),
        (["Marseille"], "Marseille"),
    ]
)
def test_t_ville(values, expected):
    df = pd.DataFrame({"ville": values})
    record = DummyRecord()

    transformer = TVille()
    result = transformer(df, record)

    assert result.ville == expected


def test_t_ville_empty_df(capsys):
    df = pd.DataFrame(columns=["ville"])
    record = DummyRecord()

    transformer = TVille()
    result = transformer(df, record)

    assert result.ville is None
    assert "DataFrame fourni est vide" in capsys.readouterr().out
