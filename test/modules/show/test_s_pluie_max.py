import pytest
from p_meteo.modules.show.s_pluie_max import SPluieMax


class DummyRecord:
    pass


def test_s_pluie_max_display(capsys):
    record = DummyRecord()
    record.pluie_max = 12.3

    viewer = SPluieMax(record)
    viewer.display()

    captured = capsys.readouterr().out
    assert "🌧️💦 Pluie max : 12.3" in captured
