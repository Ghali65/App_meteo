"""
Page Streamlit dédiée à l’affichage météo.

Cette interface permet :
- de sélectionner une ou plusieurs stations météo
- d’extraire les données via l’API (ExtractCommand)
- d’appliquer dynamiquement les transformers selon les KPIs choisis
- de construire une LinkedList de viewers Streamlit
- d’afficher les résultats sous forme de tableau HTML

Toute la logique métier (extraction, transformation, mapping KPI → transformer)
est déléguée aux modules spécialisés ; ce fichier gère uniquement l’UI.
"""

import pandas as pd
import streamlit as st

# Commandes extract / transform
from modules.command import ExtractCommand, TransformCommand
from modules.extract.call_api import CallApi
from modules.extract.to_dataframe import ToDataFrame

# LinkedList builder (version Streamlit)
from modules.streamlit_mod.st_show.st_build_viewer_list import build_streamlit_viewer_list

# Transformers
from modules.transform.transformer_registry import TRANSFORMER_REGISTRY


def show_weather(config):
    """
    Page Streamlit d’affichage météo.

    Fonctionnement :
    - sélection des stations
    - extraction des données via API
    - transformation dynamique selon les KPIs sélectionnés
    - construction d’une LinkedList de viewers Streamlit
    - affichage sous forme de tableau HTML
    """
    st.subheader("📡 Sélection des stations")

    # ---------------------------------------------------------
    # Chargement des stations depuis le CSV
    # ---------------------------------------------------------
    csv_path = config.get_value("csv_path")
    stations_df = pd.read_csv(csv_path)
    mapping = dict(zip(stations_df["dataset_id"], stations_df["ville"]))

    options = stations_df["dataset_id"].tolist()
    dataset_ids = st.multiselect("Stations disponibles :", options)

    # KPIs sélectionnés (configurable)
    selected_kpis = config.get_selected_kpis()

    # ---------------------------------------------------------
    # Boucle sur les stations sélectionnées
    # ---------------------------------------------------------
    if dataset_ids:
        for dataset_id in dataset_ids:
            st.subheader(f"📍 Station : {dataset_id}")

            # -----------------------------
            # EXTRACT
            # -----------------------------
            df = ExtractCommand(dataset_id, CallApi, ToDataFrame, mapping).execute()

            # -----------------------------
            # TRANSFORM (dynamique selon KPIs)
            # -----------------------------
            transformers = [
                TRANSFORMER_REGISTRY[kpi]()
                for kpi in selected_kpis
                if kpi in TRANSFORMER_REGISTRY
            ]

            record = TransformCommand(df, transformers).execute()

            # -----------------------------
            # VIEWERS (LinkedList Streamlit)
            # -----------------------------
            linked_list = build_streamlit_viewer_list(record, selected_kpis)

            # -----------------------------
            # TABLEAU HTML
            # -----------------------------
            rows = ""
            maillon = linked_list.premier_maillon

            while maillon:
                label, value = maillon.get_value().get_value()
                rows += f"<tr><td>{label}</td><td>{value}</td></tr>"
                maillon = maillon.get_suivant()

            html = f"<table>{rows}</table>"
            st.markdown(html, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # Navigation bas de page
    # ---------------------------------------------------------
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
