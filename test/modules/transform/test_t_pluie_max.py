import pandas as pd
import pytest
from p_meteo.modules.transform.t_pluie_max import TPluieMax


class DummyRecord:
    pass


@pytest.mark.parametrize(
    "values, expected",
    [
        ([5.2], 5.2),
        ([0.0], 0.0),
        ([12.3], 12.3),
    ]
)
def test_t_pluie_max(values, expected):
    df = pd.DataFrame({"pluie_intensite_max": values})
    record = DummyRecord()

    transformer = TPluieMax()
    result = transformer(df, record)

    assert result.pluie_max == expected


def test_t_pluie_max_empty_df(capsys):
    df = pd.DataFrame(columns=["pluie_intensite_max"])
    record = DummyRecord()

    transformer = TPluieMax()
    result = transformer(df, record)

    assert result.pluie_max is None
    assert "DataFrame vide" in capsys.readouterr().out
