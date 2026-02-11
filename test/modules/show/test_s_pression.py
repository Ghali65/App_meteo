import pytest
from p_meteo.modules.show.s_pression import SPression


class DummyRecord:
    pass


def test_s_pression_display(capsys):
    record = DummyRecord()
    record.pression = 1013

    viewer = SPression(record)
    viewer.display()

    captured = capsys.readouterr().out
    assert "📊 Pression : 1013" in captured
