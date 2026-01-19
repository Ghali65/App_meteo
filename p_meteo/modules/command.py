"""
Implémentation du Command Pattern pour orchestrer le pipeline :
Extraction → Transformation → Affichage.
"""

from typing import Any, List

from .show.build_viewer_list import build_viewer_list
from .transform.record import Record
from .configuration import Configuration


class Command:
    """Classe de base pour toutes les commandes du pipeline."""

    def execute(self) -> Any:
        """Méthode à implémenter dans chaque commande concrète."""
        raise NotImplementedError("La méthode execute() doit être implémentée.")


class ExtractCommand(Command):
    """Commande d'extraction : API → JSON → DataFrame."""

    def __init__(self, dataset_id: str, call_api, to_data_frame, mapping: dict) -> None:
        """ 
        Initialise la commande d'extraction. 
        Args: 
            dataset_id: Identifiant de la station météo. 
            call_api: Classe responsable de l'appel API. 
            to_data_frame: Classe responsable de la conversion JSON → DataFrame. 
            mapping: Dictionnaire dataset_id → nom de ville
        """
        self.dataset_id = dataset_id
        self.call_api = call_api
        self.to_data_frame = to_data_frame
        self.mapping = mapping
        self.df = None

    def execute(self):
        """ Exécute l'extraction :
        - appel API
        - récupération des données brutes
        - conversion en DataFrame 
        
        Returns: 
            DataFrame contenant les données météo normalisées. 
        """
        api = self.call_api(self.dataset_id)
        api.fetch()

        ville = self.mapping.get(self.dataset_id, "Inconnue")

        converter = self.to_data_frame(api.data, self.dataset_id, ville)
        self.df = converter.convert()

        return self.df


class TransformCommand(Command):
    """Commande de transformation : DataFrame → Record enrichi."""

    def __init__(self, df, transformers: List[Any]) -> None:
        """ Initialise la commande de transformation. 

        Args: 
            df: DataFrame contenant les données brutes. 
            transformers: Liste de fonctions ou classes appliquant les KPI. 
        """
        self.df = df
        self.transformers = transformers

    def execute(self) -> Record:
        """ Applique séquentiellement les transformers pour enrichir un Record.
        Returns:
            Record contenant tous les KPI calculés. 
        """
        config = Configuration()
        kpi_mapping = config.get_kpi_mapping()

        record = Record(kpi_mapping)

        for transformer in self.transformers:
            record = transformer(self.df, record)

        return record


class ShowCommand(Command):
    """Commande d'affichage : Record → Viewers console."""

    def __init__(self, record: Record, selected_kpis: List[str]) -> None:
        """ Initialise la commande d'affichage. 

        Args:
            record: Objet Record contenant les KPI.
            selected_kpis: Liste des KPI à afficher.
        """
        self.record = record
        self.selected_kpis = selected_kpis

    def execute(self) -> None:
        """ 
        Construit une LinkedList de viewers console et affiche les KPI. 
        """
        linked_list = build_viewer_list(self.record, self.selected_kpis)
        linked_list.display_all()
