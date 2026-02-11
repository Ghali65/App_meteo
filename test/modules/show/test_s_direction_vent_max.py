import pytest
from p_meteo.modules.show.s_direction_vent_max import SDirectionVentMax


class DummyRecord:
    pass


def test_s_direction_vent_max_display(capsys):
    record = DummyRecord()
    record.direction_vent_max = 270

    viewer = SDirectionVentMax(record)
    viewer.display()

    captured = capsys.readouterr().out
    assert "🧭 Direction vent max : 270" in captured
