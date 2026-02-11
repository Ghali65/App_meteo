import pytest
from p_meteo.modules.show.s_temperature import STemperature


class DummyRecord:
    pass


def test_s_temperature_display(capsys):
    record = DummyRecord()
    record.temperature = 22.5

    viewer = STemperature(record)
    viewer.display()

    captured = capsys.readouterr().out
    assert "🌡️ Température : 22.5" in captured
