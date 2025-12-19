from typing import List
import pandas as pd

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

# Show
from .modules.show.s_heure_maj import SHeureMaj
from .modules.show.s_humidite import SHumidite
from .modules.show.s_pression import SPression
from .modules.show.s_station_id import SStationId
from .modules.show.s_temperature import STemperature
from .modules.show.s_ville import SVille

# Commands
from .modules.command import ExtractCommand, TransformCommand, ShowCommand

# LinkedList
from .modules.chained.linked_list import Link, LinkedList


def main() -> None:

    configuration = Configuration()
    csv_path: str = configuration.get_value("csv_path")

    selector = StationSelector(csv_path)
    dataset_ids: List[str] = selector.choose()

    for dataset_id in dataset_ids:
        print(f"\n=== Traitement de la station {dataset_id} ===")

        '''les classes ExtractCommand, TransformCommand, ShowCommand font partis d'un design pattern command'''
        # 1) Extraction
        df = ExtractCommand(dataset_id, CallApi, ToDataFrame).execute()

        # 2) Transformation via TransformCommand
        transformers = [
            TVille,
            TStationId,
            TTemperature,
            THeureMaj,
            THumidite,
            TPression,
        ]

        transformed = TransformCommand(df, transformers).execute()

        # 3) Shower automatiques
        shower_classes = [
            SVille,
            SStationId,
            STemperature,
            SHeureMaj,
            SHumidite,
            SPression,
        ]

        showers = [
            viewer_class(transformed_obj)
            for transformed_obj, viewer_class in zip(transformed, shower_classes)
        ]

        # 4) Affichage
        ShowCommand(showers, LinkedList, Link).execute()


if __name__ == "__main__":
    main()
