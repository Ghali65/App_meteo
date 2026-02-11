import pandas as pd
import pytest
from p_meteo.modules.transform.t_pression import TPression


class DummyRecord:
    pass


@pytest.mark.parametrize(
    "values, expected",
    [
        ([98700], 98700),
        ([99002], 99002),
        ([97500], 97500),
    ]
)
def test_t_pression(values, expected):
    df = pd.DataFrame({"pression": values})
    record = DummyRecord()

    transformer = TPression()
    result = transformer(df, record)

    assert result.pression == expected


def test_t_pression_empty_df(capsys):
    df = pd.DataFrame(columns=["pression"])
    record = DummyRecord()

    transformer = TPression()
    result = transformer(df, record)

    assert result.pression is None
    assert "DataFrame fourni est vide" in capsys.readouterr().out
