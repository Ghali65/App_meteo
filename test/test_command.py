import pandas as pd
from unittest.mock import MagicMock
from p_meteo.modules.command import ExtractCommand, TransformCommand, ShowCommand


# ============================================================
#  EXTRACT COMMAND
# ============================================================

def test_extract_command():
    # Mock API
    api_instance = MagicMock()
    api_instance.data = {"value": 42}

    ApiMock = MagicMock(return_value=api_instance)

    # Mock ToDataFrame
    df = pd.DataFrame({"value": [42], "ville": ["Toulouse"]})
    converter_instance = MagicMock()
    converter_instance.convert.return_value = df

    ToDataFrameMock = MagicMock(return_value=converter_instance)

    mapping = {"station_1": "Toulouse"}

    cmd = ExtractCommand(
        dataset_id="station_1",
        call_api=ApiMock,
        to_data_frame=ToDataFrameMock,
        mapping=mapping,
    )

    result_df = cmd.execute()

    # Vérifications
    ApiMock.assert_called_once_with("station_1")
    api_instance.fetch.assert_called_once()

    ToDataFrameMock.assert_called_once_with({"value": 42}, "station_1", "Toulouse")
    converter_instance.convert.assert_called_once()

    assert result_df.equals(df)


# ============================================================
#  TRANSFORM COMMAND
# ============================================================

def test_transform_command():
    df = pd.DataFrame({"x": [10]})

    # On crée deux mocks
    t1 = MagicMock()
    t2 = MagicMock()

    # record initial créé par TransformCommand
    # On ne le connaît pas à l'avance, donc on le capture via side_effect
    record_after_t1 = MagicMock()
    record_after_t2 = MagicMock()

    # t1 renvoie record_after_t1
    t1.return_value = record_after_t1

    # t2 renvoie record_after_t2
    t2.return_value = record_after_t2

    cmd = TransformCommand(df, [t1, t2])
    result = cmd.execute()

    # Vérification des appels
    # t1 doit être appelé avec le record initial (inconnu)
    t1.assert_called_once()
    initial_record_passed = t1.call_args[0][1]

    # t2 doit être appelé avec le record renvoyé par t1
    t2.assert_called_once_with(df, record_after_t1)

    # Le résultat final doit être celui renvoyé par t2
    assert result is record_after_t2

    # On vérifie que le record initial est bien un objet différent
    assert initial_record_passed is not record_after_t1


# ============================================================
#  SHOW COMMAND
# ============================================================

def test_show_command(monkeypatch):
    record = MagicMock()
    selected = ["temperature"]

    # Mock de la linked list
    linked_list = MagicMock()

    # Mock de build_viewer_list
    def fake_builder(rec, kpis):
        assert rec is record
        assert kpis == selected
        return linked_list

    monkeypatch.setattr(
        "p_meteo.modules.command.build_viewer_list",
        fake_builder
    )

    cmd = ShowCommand(record, selected)
    cmd.execute()

    linked_list.display_all.assert_called_once()
