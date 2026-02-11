import pandas as pd
import pytest
from p_meteo.modules.transform.t_temperature import TTemperature


class DummyRecord:
    pass


@pytest.mark.parametrize(
    "values, expected",
    [
        ([10], 10),
        ([0], 0),
        ([25], 25),
    ]
)
def test_t_temperature(values, expected):
    df = pd.DataFrame({"temperature_en_degre_c": values})
    record = DummyRecord()

    transformer = TTemperature()
    result = transformer(df, record)

    assert result.temperature == expected


def test_t_temperature_empty_df(capsys):
    df = pd.DataFrame(columns=["temperature_en_degre_c"])
    record = DummyRecord()

    transformer = TTemperature()
    result = transformer(df, record)

    assert result.temperature is None
    assert "DataFrame fourni est vide" in capsys.readouterr().out
