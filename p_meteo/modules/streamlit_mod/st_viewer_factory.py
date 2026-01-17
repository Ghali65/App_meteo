"""
Factory permettant de créer dynamiquement les viewers Streamlit
à partir du nom technique d’un KPI.

Fonctionnement :
- Le fichier config.json contient un mapping : nom_technique → nom_de_classe_viewer
- Ce module contient un registre Python : nom_de_classe_viewer → classe réelle
- La méthode create() combine les deux pour instancier le bon viewer Streamlit

Ce pattern permet :
- d’ajouter facilement de nouveaux viewers Streamlit
- de séparer totalement la logique d’affichage de la logique métier
- d’éviter les imports dynamiques risqués
"""

from modules.configuration import Configuration

# ----------------------------------------------------------------------
# 📦 Imports explicites des viewers Streamlit
# Chaque viewer doit être importé ici pour être disponible dans le registre.
# ----------------------------------------------------------------------
from .st_show.st_ville import St_Ville
from .st_show.st_temperature import St_Temperature
from .st_show.st_heure_maj import St_HeureMaj
from .st_show.st_humidite import St_Humidite
from .st_show.st_pression import St_Pression
from .st_show.st_pluie import St_Pluie
from .st_show.st_pluie_max import St_PluieMax
from .st_show.st_vent_moyen import St_VentMoyen
from .st_show.st_rafale_max import St_RafaleMax
from .st_show.st_direction_vent_max import St_DirectionVentMax
from .st_show.st_direction_vent_max_deg import St_DirectionVentMaxDeg
from .st_show.st_direction_vent_moyen import St_DirectionVentMoyen


class StreamlitViewerFactory:
    """
    Factory responsable de créer un viewer Streamlit à partir d’un nom technique.

    Exemple :
        viewer_type = "temperature"
        → config.json donne "STemperature"
        → _class_mapping donne la classe St_Temperature
        → on retourne St_Temperature(record)
    """

    # ------------------------------------------------------------------
    # 🗂️ Registre Python : nom_de_classe → classe réelle
    # Ce dictionnaire doit contenir toutes les classes importées ci-dessus.
    # ------------------------------------------------------------------
    _class_mapping = {
        "SVille": St_Ville,
        "SHeureMaj": St_HeureMaj,
        "STemperature": St_Temperature,
        "SHumidite": St_Humidite,
        "SPression": St_Pression,
        "SPluie": St_Pluie,
        "SPluieMax": St_PluieMax,
        "SVentMoyen": St_VentMoyen,
        "SRafaleMax": St_RafaleMax,
        "SDirectionVentMax": St_DirectionVentMax,
        "SDirectionVentMaxDeg": St_DirectionVentMaxDeg,
        "SDirectionVentMoyen": St_DirectionVentMoyen,
    }

    @classmethod
    def create(cls, viewer_type: str, record):
        """
        Crée et retourne une instance de viewer Streamlit correspondant au KPI demandé.

        Étapes :
        1. Lire le mapping JSON (nom_technique → nom_de_classe_viewer)
        2. Vérifier que le KPI existe dans le mapping
        3. Vérifier que la classe existe dans _class_mapping
        4. Instancier la classe avec le record

        Args:
            viewer_type (str): nom technique du KPI (ex: "temperature")
            record (Record): objet Record contenant les valeurs transformées

        Returns:
            Instance d’un viewer Streamlit (ex: St_Temperature(record))

        Raises:
            ValueError: si le KPI ou la classe viewer n’existe pas
        """
        config = Configuration()
        viewer_mapping = config.get_viewer_mapping()

        # Vérifie que le KPI existe dans le mapping JSON
        if viewer_type not in viewer_mapping:
            raise ValueError(f"Viewer Streamlit inconnu : {viewer_type}")

        class_name = viewer_mapping[viewer_type]

        # Vérifie que la classe existe dans le registre Python
        if class_name not in cls._class_mapping:
            raise ValueError(f"Classe viewer inconnue : {class_name}")

        return cls._class_mapping[class_name](record)