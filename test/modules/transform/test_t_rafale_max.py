import pandas as pd
import pytest
from p_meteo.modules.transform.t_rafale_max import TRafaleMax


class DummyRecord:
    pass


@pytest.mark.parametrize(
    "values, expected",
    [
        ([50], 50),
        ([10], 10),
        ([90], 90),
    ]
)
def test_t_rafale_max(values, expected):
    df = pd.DataFrame({"force_rafale_max": values})
    record = DummyRecord()

    transformer = TRafaleMax()
    result = transformer(df, record)

    assert result.rafale_max == expected


def test_t_rafale_max_empty_df(capsys):
    df = pd.DataFrame(columns=["force_rafale_max"])
    record = DummyRecord()

    transformer = TRafaleMax()
    result = transformer(df, record)

    assert result.rafale_max is None
    assert "DataFrame vide" in capsys.readouterr().out
