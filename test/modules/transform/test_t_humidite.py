import pandas as pd
import pytest
from p_meteo.modules.transform.t_humidite import THumidite


class DummyRecord:
    pass


@pytest.mark.parametrize(
    "values, expected",
    [
        ([30], 30),
        ([75], 75),
        ([0], 0),
    ]
)
def test_t_humidite(values, expected):
    df = pd.DataFrame({"humidite": values})
    record = DummyRecord()

    transformer = THumidite()
    result = transformer(df, record)

    assert result.humidite == expected


def test_t_humidite_empty_df(capsys):
    df = pd.DataFrame(columns=["humidite"])
    record = DummyRecord()

    transformer = THumidite()
    result = transformer(df, record)

    assert result.humidite is None
    assert "DataFrame fourni est vide" in capsys.readouterr().out
