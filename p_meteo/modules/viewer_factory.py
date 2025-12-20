from .show.s_heure_maj import SHeureMaj
from .show.s_humidite import SHumidite
from .show.s_pression import SPression
from .show.s_station_id import SStationId
from .show.s_temperature import STemperature
from .show.s_ville import SVille


class ViewerFactory:
    """
    Factory Method permettant de créer dynamiquement
    un viewer d'affichage à partir d'un type donné.
    """

    _mapping = {
        "heure": SHeureMaj,
        "humidite": SHumidite,
        "pression": SPression,
        "station": SStationId,
        "temperature": STemperature,
        "ville": SVille,
    }

    @classmethod
    def create(cls, viewer_type: str, record):
        """
        Instancie et retourne le viewer correspondant au type demandé.

        Args:
            viewer_type (str): Nom du viewer à créer.
            record: Objet Record contenant les données météo.

        Returns:
            Instance d'une classe SXXX correspondant au type demandé.

        Raises:
            ValueError: Si le type demandé n'existe pas dans le mapping.
        """
        if viewer_type not in cls._mapping:
            raise ValueError(f"Viewer inconnu : {viewer_type}")

        return cls._mapping[viewer_type](record)
