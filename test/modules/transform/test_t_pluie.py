import pandas as pd
import pytest
from p_meteo.modules.transform.t_pluie import TPluie


class DummyRecord:
    pass


@pytest.mark.parametrize(
    "values, expected",
    [
        ([0.0], 0.0),
        ([10.5], 10.5),
        ([7.7], 7.7),
    ]
)
def test_t_pluie(values, expected):
    df = pd.DataFrame({"pluie": values})
    record = DummyRecord()

    transformer = TPluie()
    result = transformer(df, record)

    assert result.pluie == expected


def test_t_pluie_empty_df(capsys):
    df = pd.DataFrame(columns=["pluie"])
    record = DummyRecord()

    transformer = TPluie()
    result = transformer(df, record)

    assert result.pluie is None
    assert "DataFrame vide" in capsys.readouterr().out
