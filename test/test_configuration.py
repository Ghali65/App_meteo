import json
import builtins
import pytest
from p_meteo.modules.configuration import Configuration


# ----------------------------------------------------------------------
# 🔄 FIXTURE : reset du Singleton avant chaque test
# ----------------------------------------------------------------------
@pytest.fixture(autouse=True)
def reset_singleton():
    Configuration._instance = None
    Configuration._config = {}
    yield
    Configuration._instance = None
    Configuration._config = {}


# ----------------------------------------------------------------------
# 🔥 TESTS DU SINGLETON ET DU CHARGEMENT JSON
# ----------------------------------------------------------------------
def test_singleton_loads_json(monkeypatch):
    fake_json = {"a": 1, "b": 2}

    def fake_open(*args, **kwargs):
        from io import StringIO
        return StringIO(json.dumps(fake_json))

    monkeypatch.setattr(builtins, "open", fake_open)

    cfg1 = Configuration()
    cfg2 = Configuration()

    assert cfg1 is cfg2
    assert cfg1.all() == fake_json


def test_file_not_found(monkeypatch):
    def fake_open(*args, **kwargs):
        raise FileNotFoundError("missing")

    monkeypatch.setattr(builtins, "open", fake_open)

    with pytest.raises(FileNotFoundError):
        Configuration()


def test_invalid_json(monkeypatch):
    def fake_open(*args, **kwargs):
        from io import StringIO
        return StringIO("{ invalid json }")

    monkeypatch.setattr(builtins, "open", fake_open)

    with pytest.raises(ValueError):
        Configuration()


# ----------------------------------------------------------------------
# 🔧 TESTS DES MÉTHODES GÉNÉRIQUES
# ----------------------------------------------------------------------
def test_get_value(monkeypatch):
    monkeypatch.setattr(
        builtins, "open",
        lambda *args, **kwargs: __import__("io").StringIO('{"x": 42}')
    )

    cfg = Configuration()
    assert cfg.get_value("x") == 42
    assert cfg.get_value("missing", default="fallback") == "fallback"


def test_set_value_calls_save(monkeypatch):
    # Fake JSON initial
    monkeypatch.setattr(
        builtins, "open",
        lambda *args, **kwargs: __import__("io").StringIO("{}")
    )

    cfg = Configuration()

    # Mock save()
    called = {"ok": False}

    def fake_save():
        called["ok"] = True

    monkeypatch.setattr(cfg, "save", fake_save)

    cfg.set_value("test", 123)

    assert cfg.get_value("test") == 123
    assert called["ok"] is True


def test_save_writes_file(monkeypatch):
    # Fake JSON initial
    monkeypatch.setattr(
        builtins, "open",
        lambda *args, **kwargs: __import__("io").StringIO("{}")
    )

    cfg = Configuration()
    cfg._config = {"a": 1}

    written = {"content": ""}

    class FakeFile:
        def write(self, data):
            written["content"] += data  # <-- concaténation

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            pass

    def fake_open(*args, **kwargs):
        return FakeFile()

    monkeypatch.setattr(builtins, "open", fake_open)

    cfg.save()

    assert '"a": 1' in written["content"]




# ----------------------------------------------------------------------
# 📊 TESTS DES MÉTHODES SPÉCIALISÉES
# ----------------------------------------------------------------------
def test_selected_kpis(monkeypatch):
    monkeypatch.setattr(
        builtins, "open",
        lambda *args, **kwargs: __import__("io").StringIO('{"selected_kpis": ["a","b"]}')
    )

    cfg = Configuration()
    assert cfg.get_selected_kpis() == ["a", "b"]

    cfg.set_selected_kpis(["x", "y"])
    assert cfg.get_selected_kpis() == ["x", "y"]


def test_default_kpis(monkeypatch):
    monkeypatch.setattr(
        builtins, "open",
        lambda *args, **kwargs: __import__("io").StringIO('{"default_kpis": ["t","h"]}')
    )

    cfg = Configuration()
    assert cfg.get_default_kpis() == ["t", "h"]


def test_available_kpis(monkeypatch):
    monkeypatch.setattr(
        builtins, "open",
        lambda *args, **kwargs: __import__("io").StringIO('{"available_kpis": {"temp":"Température"}}')
    )

    cfg = Configuration()
    assert cfg.get_available_kpis() == {"temp": "Température"}


def test_kpi_mapping(monkeypatch):
    monkeypatch.setattr(
        builtins, "open",
        lambda *args, **kwargs: __import__("io").StringIO('{"kpi_mapping": {"temp":"T"}}')
    )

    cfg = Configuration()
    assert cfg.get_kpi_mapping() == {"temp": "T"}


def test_viewer_mapping(monkeypatch):
    monkeypatch.setattr(
        builtins, "open",
        lambda *args, **kwargs: __import__("io").StringIO('{"viewer_mapping": {"temp":"TempViewer"}}')
    )

    cfg = Configuration()
    assert cfg.get_viewer_mapping() == {"temp": "TempViewer"}
