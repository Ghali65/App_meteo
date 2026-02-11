import pytest
from p_meteo.modules.show.s_humidite import SHumidite


class DummyRecord:
    pass


def test_s_humidite_display(capsys):
    record = DummyRecord()
    record.humidite = 75

    viewer = SHumidite(record)
    viewer.display()

    captured = capsys.readouterr().out
    assert "💧 Humidité : 75" in captured
