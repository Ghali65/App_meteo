from .configuration import Configuration

# Imports explicites des viewers
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


# Dictionnaire Python : nom de classe → classe réelle
CLASS_REGISTRY = {
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
    "SDirectionVentMoyen": SDirectionVentMoyen
}


class ViewerFactory:
    """
    Crée un viewer à partir d'un nom technique.
    Exemple : "vent_moyen" → SVentMoyen(record)
    """

    @classmethod
    def create(cls, kpi_name: str, record):
        config = Configuration()
        viewer_mapping = config.get_viewer_mapping()

        # Vérifie que le KPI existe dans le mapping JSON
        if kpi_name not in viewer_mapping:
            raise ValueError(f"Viewer inconnu : {kpi_name}")

        class_name = viewer_mapping[kpi_name]

        # Vérifie que la classe existe dans le registre Python
        if class_name not in CLASS_REGISTRY:
            raise ValueError(f"Classe viewer inconnue : {class_name}")

        viewer_class = CLASS_REGISTRY[class_name]
        return viewer_class(record)
