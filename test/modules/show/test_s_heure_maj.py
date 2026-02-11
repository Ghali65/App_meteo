import pytest
from p_meteo.modules.show.s_heure_maj import SHeureMaj


class DummyRecord:
    pass


def test_s_heure_maj_display(capsys):
    record = DummyRecord()
    record.heure_maj = "15-01-2024 à 14h30"

    viewer = SHeureMaj(record)
    viewer.display()

    captured = capsys.readouterr().out
    assert "🕒 Dernière mise à jour : 15-01-2024 à 14h30" in captured
