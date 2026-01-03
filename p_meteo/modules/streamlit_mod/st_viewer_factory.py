from modules.configuration import Configuration

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
        config = Configuration()
        viewer_mapping = config.get_viewer_mapping()

        if viewer_type not in viewer_mapping:
            raise ValueError(f"Viewer Streamlit inconnu : {viewer_type}")

        class_name = viewer_mapping[viewer_type]

        if class_name not in cls._class_mapping:
            raise ValueError(f"Classe viewer inconnue : {class_name}")

        return cls._class_mapping[class_name](record)