"""
Factory permettant de créer dynamiquement les viewers console
à partir du nom technique d’un KPI.

Ce module s’appuie sur :
- le fichier config.json (mapping nom_technique → nom de classe viewer)
- un registre Python (CLASS_REGISTRY) contenant les classes réelles
- la classe Configuration pour accéder aux mappings

L’objectif est de séparer totalement la logique métier
de la logique d’affichage console.
"""

from typing import Any, Dict, Type

from .configuration import Configuration

# ----------------------------------------------------------------------
# 📦 Imports explicites des viewers console
# Chaque viewer doit être importé ici pour être disponible dans le registre.
# ----------------------------------------------------------------------
from .show.s_ville import SVille
from .show.s_heure_maj import SHeureMaj
from .show.s_temperature import STemperature
from .show.s_humidite import SHumidite
from .show.s_pression import SPression
from .show.s_pluie import SPluie
from .show.s_pluie_max import SPluieMax
from .show.s_vent_moyen import SVentMoyen
from .show.s_rafale_max import SRafaleMax
from .show.s_direction_vent_max import SDirectionVentMax
from .show.s_direction_vent_max_deg import SDirectionVentMaxDeg
from .show.s_direction_vent_moyen import SDirectionVentMoyen


# ----------------------------------------------------------------------
# 🗂️ Registre Python : nom de classe → classe réelle
# Ce dictionnaire permet de retrouver la classe viewer à instancier.
# Il doit contenir toutes les classes importées ci-dessus.
# ----------------------------------------------------------------------
CLASS_REGISTRY: Dict[str, Type] = {
    "SVille": SVille,
    "SHeureMaj": SHeureMaj,
    "STemperature": STemperature,
    "SHumidite": SHumidite,
    "SPression": SPression,
    "SPluie": SPluie,
    "SPluieMax": SPluieMax,
    "SVentMoyen": SVentMoyen,
    "SRafaleMax": SRafaleMax,
    "SDirectionVentMax": SDirectionVentMax,
    "SDirectionVentMaxDeg": SDirectionVentMaxDeg,
    "SDirectionVentMoyen": SDirectionVentMoyen,
}


class ViewerFactory:
    """
    Factory responsable de créer un viewer console à partir d’un nom technique.

    Exemple :
        kpi_name = "vent_moyen"
        → config.json donne "SVentMoyen"
        → CLASS_REGISTRY donne la classe SVentMoyen
        → on retourne SVentMoyen(record)

    Cette classe permet :
    - de découpler totalement le pipeline de l’affichage
    - d’ajouter facilement de nouveaux viewers
    - d’éviter les imports dynamiques risqués
    """

    @classmethod
    def create(cls, kpi_name: str, record: Any):
        """
        Crée et retourne une instance de viewer correspondant au KPI demandé.

        Étapes :
        1. Lire le mapping JSON (nom_technique → nom_de_classe)
        2. Vérifier que le KPI existe dans le mapping
        3. Vérifier que la classe existe dans CLASS_REGISTRY
        4. Instancier la classe avec le record

        Args:
            kpi_name (str): nom technique du KPI (ex: "temperature")
            record (Record): objet Record contenant les valeurs transformées

        Returns:
            Instance d’un viewer console (ex: STemperature(record))

        Raises:
            ValueError: si le KPI ou la classe viewer n’existe pas
        """
        config = Configuration()
        viewer_mapping = config.get_viewer_mapping()

        # Vérifie que le KPI existe dans le mapping JSON
        if kpi_name not in viewer_mapping:
            raise ValueError(f"Viewer inconnu dans config.json : {kpi_name}")

        class_name = viewer_mapping[kpi_name]

        # Vérifie que la classe existe dans le registre Python
        if class_name not in CLASS_REGISTRY:
            raise ValueError(f"Classe viewer inconnue dans CLASS_REGISTRY : {class_name}")

        viewer_class = CLASS_REGISTRY[class_name]
        return viewer_class(record)
