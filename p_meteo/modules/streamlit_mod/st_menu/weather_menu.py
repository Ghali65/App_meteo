import pandas as pd
import streamlit as st

# Configuration / commandes / extract / transform
from modules.command import ExtractCommand, TransformCommand
from modules.extract.call_api import CallApi
from modules.extract.to_dataframe import ToDataFrame

# LinkedList builder (version Streamlit)
from modules.streamlit_mod.st_show.st_build_viewer_list import build_streamlit_viewer_list

# Transformer
from modules.transform.t_ville import TVille
from modules.transform.t_temperature import TTemperature
from modules.transform.t_heure_maj import THeureMaj
from modules.transform.t_humidite import THumidite
from modules.transform.t_pression import TPression
from modules.transform.t_pluie import TPluie
from modules.transform.t_pluie_max import TPluieMax
from modules.transform.t_vent_moyen import TVentMoyen
from modules.transform.t_rafale_max import TRafaleMax
from modules.transform.t_direction_vent_max import TDirectionVentMax
from modules.transform.t_direction_vent_max_deg import TDirectionVentMaxDeg
from modules.transform.t_direction_vent_moyen import TDirectionVentMoyen

# Mapping nom technique → classe transformer
TRANSFORMER_REGISTRY = {
    "ville": TVille,
    "temperature": TTemperature,
    "heure_maj": THeureMaj,
    "humidite": THumidite,
    "pression": TPression,
    "pluie": TPluie,
    "pluie_max": TPluieMax,
    "vent_moyen": TVentMoyen,
    "rafale_max": TRafaleMax,
    "direction_vent_max": TDirectionVentMax,
    "direction_vent_max_deg": TDirectionVentMaxDeg,
    "direction_vent_moyen": TDirectionVentMoyen,
}


def show_weather(config):
    st.subheader("📡 Sélection des stations")

    # Récupération des stations depuis le CSV
    csv_path = config.get_value("csv_path")
    stations_df = pd.read_csv(csv_path)
    mapping = dict(zip(stations_df["dataset_id"], stations_df["ville"]))

    options = stations_df["dataset_id"].tolist()
    dataset_ids = st.multiselect("Stations disponibles :", options)

    # KPIs sélectionnés (configurable)
    selected_kpis = config.get_selected_kpis()

    if dataset_ids:
        for dataset_id in dataset_ids:
            st.subheader(f"📍 Station : {dataset_id}")

            # Extract
            df = ExtractCommand(dataset_id, CallApi, ToDataFrame, mapping).execute()

            # Build transformers dynamiquement à partir des KPIs
            transformers = [
                TRANSFORMER_REGISTRY[kpi]() 
                for kpi in selected_kpis 
                if kpi in TRANSFORMER_REGISTRY
            ]

            # Transform
            record = TransformCommand(df, transformers).execute()

            # Build LinkedList pour affichage Streamlit
            linked_list = build_streamlit_viewer_list(record, selected_kpis)

            # Construction du tableau HTML
            rows = ""
            maillon = linked_list.premier_maillon
            while maillon:
                label, value = maillon.get_value().get_value()
                rows += f"<tr><td>{label}</td><td>{value}</td></tr>"
                maillon = maillon.get_suivant()

            html = f"<table>{rows}</table>"
            st.markdown(html, unsafe_allow_html=True)

    # Navigation bas de page
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🏠 Retour menu principal"):
            st.session_state["mode"] = "menu"
            st.rerun()
    with col2:
        if st.button("🎛️ Modifier les KPIs"):
            st.session_state["mode"] = "custom"
            st.rerun()
    with col3:
        if st.button("❌ Quitter"):
            st.session_state["mode"] = "exit"
            st.rerun()