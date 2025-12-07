import json
import pandas as pd
import streamlit as st
from typing import Dict, List

# Import des viewers adaptés à Streamlit
from modules.streamlit_mod.st_temperature import St_Temperature
from modules.streamlit_mod.st_heure_maj import St_HeureMaj
from modules.streamlit_mod.st_humidite import St_Humidite
from modules.streamlit_mod.st_pression import St_Pression
from modules.streamlit_mod.st_ville import St_Ville

# Import des modules extract / transform
from modules.extract.call_api import CallApi
from modules.extract.to_dataframe import ToDataFrame
from modules.transform.t_temperature import TTemperature
from modules.transform.t_ville import TVille
from modules.transform.t_humidite import THumidite
from modules.transform.t_pression import TPression
from modules.transform.t_heure_maj import THeureMaj

# LinkedList pour garder la logique de pipeline
from modules.chained.linked_list import Link, LinkedList


def run_app() -> None:
    """
    Version Streamlit de l'application météo.
    """

    # Charger la configuration
    with open("p_meteo/config.json", "r", encoding="utf-8") as f:
        config: Dict[str, str] = json.load(f)

    csv_path: str = config["csv_path"]

    # Charger les stations disponibles
    stations_df: pd.DataFrame = pd.read_csv(csv_path)

    # Interface Streamlit
    st.title("🌤️ Application Météo")
    st.write("Sélectionnez une ou plusieurs stations pour afficher les données météo.")

    options: List[str] = stations_df["dataset_id"].tolist()
    dataset_ids: List[str] = st.multiselect("Stations disponibles :", options)

    # Parcours des stations sélectionnées
    if dataset_ids:
        for dataset_id in dataset_ids:
            st.subheader(f"📡 Station : {dataset_id}")

            # Extraction
            api: CallApi = CallApi(dataset_id)
            api.fetch()

            converter: ToDataFrame = ToDataFrame(api.data, dataset_id)
            df: pd.DataFrame = converter.convert()

            # Transformation
            extract_temp: TTemperature = TTemperature(df)
            extract_ville: TVille = TVille(df)
            extract_humidite: THumidite = THumidite(df)
            extract_pression: TPression = TPression(df)
            extract_heure_maj: THeureMaj = THeureMaj(df)

            # Viewers Streamlit
            viewer_ville: St_Ville = St_Ville(extract_ville)
            viewer_temp: St_Temperature = St_Temperature(extract_temp)
            viewer_humidite: St_Humidite = St_Humidite(extract_humidite)
            viewer_pression: St_Pression = St_Pression(extract_pression)
            viewer_heure_maj: St_HeureMaj = St_HeureMaj(extract_heure_maj)

            # Pipeline via LinkedList
            linked_list: LinkedList = LinkedList(Link(viewer_ville))
            linked_list.ajouter_maillon(Link(viewer_temp))
            linked_list.ajouter_maillon(Link(viewer_humidite))
            linked_list.ajouter_maillon(Link(viewer_pression))
            linked_list.ajouter_maillon(Link(viewer_heure_maj))

            # Affichage Streamlit
            maillon = linked_list.premier_maillon
            while maillon is not None:
                valeur = maillon.get_value()
                if hasattr(valeur, "display"):
                    valeur.display()  # chaque viewer utilise st.write / st.metric
                maillon = maillon.get_suivant()


if __name__ == "__main__":
    run_app()
