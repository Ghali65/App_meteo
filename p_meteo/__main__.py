import json
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
    """Script principal pour exécuter l'extraction, la transformation et l'affichage."""

    # Charger la configuration
    with open("p_meteo/config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    csv_path = config["csv_path"]

    # Sélection des stations (une ou plusieurs)
    selector = StationSelector(csv_path)
    dataset_ids = selector.choose()  # retourne une liste de dataset_id

    # Parcours des stations sélectionnées
    for dataset_id in dataset_ids:
        print(f"\n=== Traitement de la station {dataset_id} ===")

        # Étapes d'extraction
        api = CallApi(dataset_id)
        api.fetch()

        converter = ToDataFrame(api.data, dataset_id)
        df = converter.convert()

        # Transformation
        extract_temp = TTemperature(df)
        extract_heure_maj = THeureMaj(df)
        extract_pression = TPression(df)
        extract_station_id = TStationId(df)
        extract_ville = TVille(df)
        extract_humidite = THumidite(df)

        # Viewers
        viewer_temp = STemperature(extract_temp)
        viewer_heure_maj = SHeureMaj(extract_heure_maj)
        viewer_pression = SPression(extract_pression)
        viewer_station_id = SStationId(extract_station_id)
        viewer_ville = SVille(extract_ville)
        viewer_humidite = SHumidite(extract_humidite)

        # Pipeline via LinkedList
        linked_list = LinkedList(Link(viewer_ville))
        linked_list.ajouter_maillon(Link(viewer_station_id))
        linked_list.ajouter_maillon(Link(viewer_temp))
        linked_list.ajouter_maillon(Link(viewer_humidite))
        linked_list.ajouter_maillon(Link(viewer_pression))
        linked_list.ajouter_maillon(Link(viewer_heure_maj))

        # Affichage des résultats
        linked_list.afficher_liste()

if __name__ == "__main__":
    main()
