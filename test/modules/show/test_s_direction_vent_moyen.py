import pytest
from p_meteo.modules.show.s_direction_vent_moyen import SDirectionVentMoyen


class DummyRecord:
    pass


def test_s_direction_vent_moyen_display(capsys):
    record = DummyRecord()
    record.direction_vent_moyen = 315

    viewer = SDirectionVentMoyen(record)
    viewer.display()

    captured = capsys.readouterr().out
    assert "🧭➡️ Direction vent moyen : 315" in captured
