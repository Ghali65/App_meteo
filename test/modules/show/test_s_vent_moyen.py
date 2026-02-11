import pytest
from p_meteo.modules.show.s_vent_moyen import SVentMoyen


class DummyRecord:
    pass


def test_s_vent_moyen_display(capsys):
    record = DummyRecord()
    record.vent_moyen = 15

    viewer = SVentMoyen(record)
    viewer.display()

    captured = capsys.readouterr().out
    assert "🍃 Vent moyen : 15" in captured
