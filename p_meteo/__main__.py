from typing import List
import pandas as pd

# chargement du menu principal
from .modules.menu.main_menu import main_menu

from .modules.configuration import Configuration
from .modules.extract.station_selector import StationSelector
from .modules.extract.call_api import CallApi
from .modules.extract.to_dataframe import ToDataFrame

# Transform
from .modules.transform.t_heure_maj import THeureMaj
from .modules.transform.t_humidite import THumidite
from .modules.transform.t_pression import TPression
from .modules.transform.t_station_id import TStationId
from .modules.transform.t_temperature import TTemperature
from .modules.transform.t_ville import TVille

# Commands
from .modules.command import ExtractCommand, TransformCommand, ShowCommand


def main() -> None:
    action = main_menu() 
    
    if action == "show_weather": 
        run_weather_pipeline() # fonction à créer (simple) 
    elif action == "select_kpis": 
        run_kpi_selection_menu() # étape 2 
    elif action == "admin_mode": 
        run_admin_menu() # étape 3

def run_weather_pipeline():
    configuration = Configuration()
    csv_path: str = configuration.get_value("csv_path")

    # Chargement du CSV
    stations_df = pd.read_csv(csv_path)
    mapping = dict(zip(stations_df["dataset_id"], stations_df["Ville"]))

    # Sélection des stations
    selector = StationSelector(csv_path)
    dataset_ids: List[str] = selector.choose()

    # Pipeline pour chaque station
    for dataset_id in dataset_ids:
        print(f"\n=== Traitement de la station {dataset_id} ===")

        # 1) Extraction
        df = ExtractCommand(dataset_id, CallApi, ToDataFrame, mapping).execute()

        # 2) Transformation
        transformers = [
            TVille(),
            TStationId(),
            TTemperature(),
            THeureMaj(),
            THumidite(),
            TPression(),
        ]

        record = TransformCommand(df, transformers).execute()

        # 3) Affichage
        ShowCommand(record).execute()


if __name__ == "__main__":
    main()
