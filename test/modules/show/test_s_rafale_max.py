import pytest
from p_meteo.modules.show.s_rafale_max import SRafaleMax


class DummyRecord:
    pass


def test_s_rafale_max_display(capsys):
    record = DummyRecord()
    record.rafale_max = 80

    viewer = SRafaleMax(record)
    viewer.display()

    captured = capsys.readouterr().out
    assert "💨 Rafale max : 80" in captured
