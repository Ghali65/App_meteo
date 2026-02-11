import pytest
from p_meteo.modules.show.s_direction_vent_max_deg import SDirectionVentMaxDeg


class DummyRecord:
    pass


def test_s_direction_vent_max_deg_display(capsys):
    record = DummyRecord()
    record.direction_vent_max_deg = 120

    viewer = SDirectionVentMaxDeg(record)
    viewer.display()

    captured = capsys.readouterr().out
    assert "🧭📐 Direction vent max (°) : 120" in captured
