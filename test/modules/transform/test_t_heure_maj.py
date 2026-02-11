import pandas as pd
import pytest
from p_meteo.modules.transform.t_heure_maj import THeureMaj


class DummyRecord:
    pass


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2024-01-15T14:30:00", "15-01-2024 à 14h30"),
        ("2023-12-31T23:59:00", "31-12-2023 à 23h59"),
        ("2025-06-01T00:05:00", "01-06-2025 à 00h05"),
    ]
)
def test_t_heure_maj_valid(value, expected):
    df = pd.DataFrame({"heure_de_paris": [value]})
    record = DummyRecord()

    transformer = THeureMaj()
    result = transformer(df, record)

    assert result.heure_maj == expected


def test_t_heure_maj_invalid_format():
    df = pd.DataFrame({"heure_de_paris": ["not-a-date"]})
    record = DummyRecord()

    transformer = THeureMaj()
    result = transformer(df, record)

    assert result.heure_maj == "not-a-date"


def test_t_heure_maj_empty_df(capsys):
    df = pd.DataFrame(columns=["heure_de_paris"])
    record = DummyRecord()

    transformer = THeureMaj()
    result = transformer(df, record)

    assert result.heure_maj is None
    assert "DataFrame fourni est vide" in capsys.readouterr().out
