import json
import pandas as pd
import streamlit as st
from typing import Dict, List

# Extract / Transform
from modules.extract.call_api import CallApi
from modules.extract.to_dataframe import ToDataFrame

from modules.transform.t_temperature import TTemperature
from modules.transform.t_ville import TVille
from modules.transform.t_humidite import THumidite
from modules.transform.t_pression import TPression
from modules.transform.t_heure_maj import THeureMaj

# Commands
from modules.command import ExtractCommand, TransformCommand

# LinkedList builder (version Streamlit)
from modules.streamlit_mod.st_build_viewer_list import build_streamlit_viewer_list


def run_app() -> None:
    """
    Version Streamlit utilisant le même pipeline que la version CLI :
    Extract → Transform (Record) → Show (Factory + LinkedList)
    """

    # Charger la configuration
    with open("p_meteo/config.json", "r", encoding="utf-8") as f:
        config: Dict[str, str] = json.load(f)

    csv_path: str = config["csv_path"]

    # Charger les stations disponibles
    stations_df: pd.DataFrame = pd.read_csv(csv_path)

    # Construire le mapping dataset_id -> Ville
    mapping = dict(zip(stations_df["dataset_id"], stations_df["Ville"]))

    # Interface Streamlit
    st.title("🌤️ Application Météo")
    st.write("Sélectionnez une ou plusieurs stations pour afficher les données météo.")

    options: List[str] = stations_df["dataset_id"].tolist()
    dataset_ids: List[str] = st.multiselect("Stations disponibles :", options)

    if dataset_ids:
        for dataset_id in dataset_ids:
            st.subheader(f"📡 Station : {dataset_id}")

            # 1) EXTRACT
            df = ExtractCommand(dataset_id, CallApi, ToDataFrame, mapping).execute()

            # 2) TRANSFORM → Record
            transformers = [
                TVille(),
                TTemperature(),
                THeureMaj(),
                THumidite(),
                TPression(),
            ]

            record = TransformCommand(df, transformers).execute()

            # 3) BUILD LINKEDLIST (Factory Streamlit)
            linked_list = build_streamlit_viewer_list(record)

            # 4) AFFICHAGE STREAMLIT
            maillon = linked_list.premier_maillon
            while maillon is not None:
                viewer = maillon.get_value()
                viewer.display()
                maillon = maillon.get_suivant()


if __name__ == "__main__":
    run_app()
