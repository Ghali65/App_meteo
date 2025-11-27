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


def main() -> None:
    """Script principal pour exécuter l'extraction, la transformation et l'affichage."""

    # Charger la configuration
    with open("p_meteo/config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    csv_path = config["csv_path"]

    # Étapes d'extraction
    selector = StationSelector(csv_path)
    dataset_id = selector.choose()

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

    # Affichage unitaire
    
    viewer_temp = STemperature(extract_temp)
    viewer_heure_maj = SHeureMaj(extract_heure_maj)
    viewer_pression = SPression(extract_pression)
    viewer_station_id = SStationId(extract_station_id)
    viewer_ville = SVille(extract_ville)
    viewer_humidite = SHumidite(extract_humidite)
    viewer_ville.display_ville()
    viewer_station_id.display_station_id()
    viewer_temp.display_temperature()
    viewer_humidite.display_humidite()
    viewer_pression.display_pression()
    viewer_heure_maj.display_heure_maj()

if __name__ == "__main__":
    main()
