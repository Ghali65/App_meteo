"""
Implémentation du Command Pattern pour orchestrer le pipeline :
Extraction → Transformation → Affichage.
"""

from typing import Any, List

from p_meteo.modules.show.build_viewer_list import build_viewer_list
from p_meteo.modules.transform.record import Record
from p_meteo.modules.configuration import Configuration


class Command:
    """Classe de base pour toutes les commandes du pipeline."""

    def execute(self) -> Any:
        raise NotImplementedError("La méthode execute() doit être implémentée.")


class ExtractCommand(Command):
    """Commande d'extraction : API → JSON → DataFrame."""

    def __init__(self, dataset_id: str, CallApi, ToDataFrame, mapping: dict) -> None:
        self.dataset_id = dataset_id
        self.CallApi = CallApi
        self.ToDataFrame = ToDataFrame
        self.mapping = mapping
        self.df = None

    def execute(self):
        api = self.CallApi(self.dataset_id)
        api.fetch()

        ville = self.mapping.get(self.dataset_id, "Inconnue")

        converter = self.ToDataFrame(api.data, self.dataset_id, ville)
        self.df = converter.convert()

        return self.df


class TransformCommand(Command):
    """Commande de transformation : DataFrame → Record enrichi."""

    def __init__(self, df, transformers: List[Any]) -> None:
        self.df = df
        self.transformers = transformers

    def execute(self) -> Record:
        config = Configuration()
        kpi_mapping = config.get_kpi_mapping()

        record = Record(kpi_mapping)

        for transformer in self.transformers:
            record = transformer(self.df, record)

        return record


class ShowCommand(Command):
    """Commande d'affichage : Record → Viewers console."""

    def __init__(self, record: Record, selected_kpis: List[str]) -> None:
        self.record = record
        self.selected_kpis = selected_kpis

    def execute(self) -> None:
        linked_list = build_viewer_list(self.record, self.selected_kpis)
        linked_list.afficher_liste()
