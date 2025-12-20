import json
import pandas as pd
import streamlit as st
from typing import Dict, List

# Viewers Streamlit
from modules.streamlit_mod.st_temperature import St_Temperature
from modules.streamlit_mod.st_heure_maj import St_HeureMaj
from modules.streamlit_mod.st_humidite import St_Humidite
from modules.streamlit_mod.st_pression import St_Pression
from modules.streamlit_mod.st_ville import St_Ville

# Extract / Transform
from modules.extract.call_api import CallApi
from modules.extract.to_dataframe import ToDataFrame
from modules.transform.t_temperature import TTemperature
from modules.transform.t_ville import TVille
from modules.transform.t_humidite import THumidite
from modules.transform.t_pression import TPression
from modules.transform.t_heure_maj import THeureMaj

# Commands
from modules.command import ExtractCommand, TransformCommand, ShowCommand

# LinkedList
from modules.chained.linked_list import Link, LinkedList


def run_app() -> None:
    """
    Version Streamlit utilisant le même pipeline Command que la version CLI.
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

    # Parcours des stations sélectionnées
    if dataset_ids:
        for dataset_id in dataset_ids:
            st.subheader(f"📡 Station : {dataset_id}")

            # 1) EXTRACT (Command Pattern)
            df = ExtractCommand(
                dataset_id,
                CallApi,
                ToDataFrame,
                mapping
            ).execute()

            # 2) TRANSFORM (Command Pattern)
            transformers = [
                TVille,
                TTemperature,
                THeureMaj,
                THumidite,
                TPression,
            ]

            transformed = TransformCommand(df, transformers).execute()

            # 3) VIEWERS STREAMLIT (équivalent ShowCommand mais adapté UI)
            viewer_classes = [
                St_Ville,
                St_Temperature,
                St_HeureMaj,
                St_Humidite,
                St_Pression,
            ]

            viewers = [
                viewer_class(transformed_obj)
                for transformed_obj, viewer_class in zip(transformed, viewer_classes)
            ]

            # 4) PIPELINE D’AFFICHAGE VIA LINKEDLIST
            linked_list = LinkedList(Link(viewers[0]))
            for viewer in viewers[1:]:
                linked_list.ajouter_maillon(Link(viewer))

            # 5) AFFICHAGE STREAMLIT
            maillon = linked_list.premier_maillon
            while maillon is not None:
                valeur = maillon.get_value()
                if hasattr(valeur, "display"):
                    valeur.display()
                maillon = maillon.get_suivant()


if __name__ == "__main__":
    run_app()
