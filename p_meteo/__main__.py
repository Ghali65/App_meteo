from typing import List
import pandas as pd

from .modules.configuration import Configuration
from .modules.extract.station_selector import StationSelector
from .modules.extract.call_api import CallApi
from .modules.extract.to_dataframe import ToDataFrame
from .modules.transform.t_heure_maj import THeureMaj
from .modules.transform.t_humidite import THumidite
from .modules.transform.t_pression import TPression
from .modules.transform.t_station_id import TStationId
from .modules.transform.t_temperature import TTemperature
from .modules.transform.t_ville import TVille
from .modules.show.s_heure_maj import SHeureMaj
from .modules.show.s_humidite import SHumidite
from .modules.show.s_pression import SPression
from .modules.show.s_station_id import SStationId
from .modules.show.s_temperature import STemperature
from .modules.show.s_ville import SVille
from .modules.chained.linked_list import Link, LinkedList


def main() -> None:
    """
    Script principal pour exécuter l'extraction, la transformation et l'affichage.
    """

    # Charger la configuration
    configuration = Configuration()
    csv_path: str = configuration.get_value("csv_path")

    # Sélection des stations (une ou plusieurs)
    selector: StationSelector = StationSelector(csv_path)
    dataset_ids: List[str] = selector.choose()  # retourne une liste de dataset_id

    # Parcours des stations sélectionnées
    for dataset_id in dataset_ids:
        print(f"\n=== Traitement de la station {dataset_id} ===")

        # Étapes d'extraction
        api: CallApi = CallApi(dataset_id)
        api.fetch()

        converter: ToDataFrame = ToDataFrame(api.data, dataset_id)
        df: pd.DataFrame = converter.convert()

        # Transformation (chaque classe retourne un objet transformé)
        extract_temp: TTemperature = TTemperature(df)
        extract_heure_maj: THeureMaj = THeureMaj(df)
        extract_pression: TPression = TPression(df)
        extract_station_id: TStationId = TStationId(df)
        extract_ville: TVille = TVille(df)
        extract_humidite: THumidite = THumidite(df)

        # Viewers (chaque viewer expose display() -> None)
        viewer_temp: STemperature = STemperature(extract_temp)
        viewer_heure_maj: SHeureMaj = SHeureMaj(extract_heure_maj)
        viewer_pression: SPression = SPression(extract_pression)
        viewer_station_id: SStationId = SStationId(extract_station_id)
        viewer_ville: SVille = SVille(extract_ville)
        viewer_humidite: SHumidite = SHumidite(extract_humidite)

        # Pipeline via LinkedList
        linked_list: LinkedList = LinkedList(Link(viewer_ville))
        linked_list.ajouter_maillon(Link(viewer_station_id))
        linked_list.ajouter_maillon(Link(viewer_temp))
        linked_list.ajouter_maillon(Link(viewer_humidite))
        linked_list.ajouter_maillon(Link(viewer_pression))
        linked_list.ajouter_maillon(Link(viewer_heure_maj))

        # Affichage des résultats
        linked_list.afficher_liste()


if __name__ == "__main__":
    main()
