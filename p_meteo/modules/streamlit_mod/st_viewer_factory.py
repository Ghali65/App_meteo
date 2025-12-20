from .st_ville import St_Ville
from .st_temperature import St_Temperature
from .st_heure_maj import St_HeureMaj
from .st_humidite import St_Humidite
from .st_pression import St_Pression

class StreamlitViewerFactory:
    """
    Factory Method pour créer les viewers Streamlit
    à partir d'un type de viewer.
    """

    _mapping = {
        "ville": St_Ville,
        "temperature": St_Temperature,
        "heure": St_HeureMaj,
        "humidite": St_Humidite,
        "pression": St_Pression,
    }

    @classmethod
    def create(cls, viewer_type: str, record):
        if viewer_type not in cls._mapping:
            raise ValueError(f"Viewer Streamlit inconnu : {viewer_type}")
        return cls._mapping[viewer_type](record)
