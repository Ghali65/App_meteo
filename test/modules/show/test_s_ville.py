import pytest
from p_meteo.modules.show.s_ville import SVille


class DummyRecord:
    pass


def test_s_ville_display(capsys):
    record = DummyRecord()
    record.ville = "Toulouse"

    viewer = SVille(record)
    viewer.display()

    captured = capsys.readouterr().out
    assert "🏙️ Ville : Toulouse" in captured
