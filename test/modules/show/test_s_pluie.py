import pytest
from p_meteo.modules.show.s_pluie import SPluie


class DummyRecord:
    pass


def test_s_pluie_display(capsys):
    record = DummyRecord()
    record.pluie = 5.7

    viewer = SPluie(record)
    viewer.display()

    captured = capsys.readouterr().out
    assert "🌧️ Pluie : 5.7" in captured
