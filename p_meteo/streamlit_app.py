import pandas as pd
import streamlit as st
from typing import Dict, List

# Configuration
from modules.configuration import Configuration

# Extract / Transform
from modules.extract.call_api import CallApi
from modules.extract.to_dataframe import ToDataFrame
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

# Commands
from modules.command import ExtractCommand, TransformCommand

# LinkedList builder (version Streamlit)
from modules.streamlit_mod.st_show.st_build_viewer_list import build_streamlit_viewer_list


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
    "direction_vent_moyen": TDirectionVentMoyen
}

def menu_button(label, description, icon, mode, button_text, button_color="#2196F3"):
    # Bloc visuel + bouton collé
    st.markdown(f"""
        <div style='
            padding: 16px;
            border: 1px solid #ddd;
            border-radius: 12px;
            background-color: #f7f9fc;
        '>
            <div style='font-size: 20px; font-weight: bold; margin-bottom: 6px;'>
                {icon} {label}
            </div>
            <div style='font-size: 14px; color: #555; margin-bottom: 8px;'>
                {description}
            </div>
    """, unsafe_allow_html=True)

    # CSS pour styliser le bouton Streamlit
    st.markdown(f"""
        <style>
        div[data-testid="stButton"] > button {{
            background-color: {button_color};
            color: white;
            width: 100%;
            height: 48px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }}
        div[data-testid="stButton"] > button:hover {{
            background-color: #1976D2;
        }}
        </style>
    """, unsafe_allow_html=True)

    # Bouton cliquable
    if st.button(button_text, key=f"btn_{mode}", use_container_width=True):
        st.session_state["mode"] = mode
        st.rerun()

    # Fin du bloc + espacement entre blocs
    st.markdown("</div><div style='height: 16px;'></div>", unsafe_allow_html=True)


def show_main_menu():
    st.title("🌤️ Application Météo")
    st.write("Bienvenue ! Choisissez une action pour commencer.\n")

    config = Configuration()
    available_kpis = config.get_available_kpis()
    current_kpis = config.get_selected_kpis()
    labels = [available_kpis.get(k, k) for k in current_kpis]
    kpi_text = ", ".join(labels)

    # Bouton météo avec KPIs actuels
    menu_button(
        label="Afficher la météo",
        description=f"KPIs actuels : {kpi_text}",
        icon="🌤️",
        mode="weather",
        button_text="Lancer la selection station avec KPI listés"
    )

    # Bouton personnalisation
    menu_button(
        label="Personnaliser les KPIs",
        description="Choisissez les KPIs que vous souhaitez afficher.",
        icon="📊",
        mode="custom",
        button_text="Accéder à la personnalisation des indicateurs et selectionner les stations"
    )

    # Bouton admin
    menu_button(
        label="Mode administrateur",
        description="Gérez les stations météo (ajout, suppression, modification).",
        icon="⚙️",
        mode="admin",
        button_text="Accéder au menu administrateur"
    )

    # Bouton quitter
    menu_button(
        label="Quitter l’application",
        description="Fermer l'application météo.",
        icon="❌",
        mode="exit",
        button_text="Quitter"
    )


def show_weather(config):
    st.subheader("📡 Sélection des stations")

    csv_path = config.get_value("csv_path")
    stations_df = pd.read_csv(csv_path)
    mapping = dict(zip(stations_df["dataset_id"], stations_df["ville"]))

    options = stations_df["dataset_id"].tolist()
    dataset_ids = st.multiselect("Stations disponibles :", options)

    selected_kpis = config.get_selected_kpis()

    if dataset_ids:
        for dataset_id in dataset_ids:
            st.subheader(f"📍 Station : {dataset_id}")
            df = ExtractCommand(dataset_id, CallApi, ToDataFrame, mapping).execute()
            transformers = [TRANSFORMER_REGISTRY[kpi]() for kpi in selected_kpis if kpi in TRANSFORMER_REGISTRY]
            record = TransformCommand(df, transformers).execute()
            linked_list = build_streamlit_viewer_list(record, selected_kpis)

            rows = ""
            maillon = linked_list.premier_maillon
            while maillon:
                label, value = maillon.get_value().get_value()
                rows += f"<tr><td>{label}</td><td>{value}</td></tr>"
                maillon = maillon.get_suivant()

            html = f"<table>{rows}</table>"
            st.markdown(html, unsafe_allow_html=True)

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

def show_kpi_customization(config):
    st.subheader("🎛️ Personnalisation des KPIs")

    available_kpis = config.get_available_kpis()
    all_kpis = list(available_kpis.keys())

    # Sélection des KPIs avec labels lisibles
    selected_kpis = st.multiselect(
        "Sélectionnez les KPIs à afficher :",
        options=all_kpis,
        default=config.get_default_kpis(),
        format_func=lambda k: available_kpis.get(k, k)
    )

    if not selected_kpis:
        st.warning("Veuillez sélectionner au moins un KPI.")
        st.stop()

    # Affichage de la sélection
    st.markdown("### ✅ KPIs sélectionnés :")
    for kpi in selected_kpis:
        label = available_kpis.get(kpi, kpi)
        st.write(f"• {label}")

    # Boutons de navigation
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🏠 Retour menu principal"):
            st.session_state["mode"] = "menu"
            st.rerun()
    with col2:
        if st.button("🌤️ Afficher la météo avec ces KPIs"):
            config.set_selected_kpis(selected_kpis)
            st.session_state["mode"] = "weather"
            st.rerun()
    with col3:
        if st.button("❌ Quitter"):
            st.session_state["mode"] = "exit"
            st.rerun()

def show_admin():
    st.subheader("⚙️ Mode administrateur")
    st.info("Le mode administrateur sera ajouté prochainement.")
    
    if st.button("🏠 Retour menu principal"):
        st.session_state["mode"] = "menu"
        st.rerun()

def run_app():
    config = Configuration()

    # Initialisation unique des KPIs au démarrage
    if "initialized" not in st.session_state:
        config.set_selected_kpis(config.get_default_kpis())
        st.session_state["initialized"] = True

    if "mode" not in st.session_state:
        st.session_state["mode"] = "menu"

    mode = st.session_state["mode"]

    if mode == "menu":
        show_main_menu()

    elif mode == "weather":
        show_weather(config)

    elif mode == "custom":
        show_kpi_customization(config)

    elif mode == "admin":
        show_admin()

    elif mode == "exit":
        st.write("👋 Merci d’avoir utilisé l’application météo.")
        st.stop()


if __name__ == "__main__":
    run_app()
