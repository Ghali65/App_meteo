import streamlit as st
from ..modules.configuration import Configuration
from modules.streamlit_mod.st_menu.menu_button import menu_button


def show_main_menu():
    """
    Menu principal Streamlit de l'application météo.

    Propose :
    - l’affichage météo
    - la personnalisation des KPIs
    - le mode administrateur
    - la fermeture de l’application
    """
    st.title("🌤️ Application Météo")
    st.write("Bienvenue ! Choisissez une action pour commencer.\n")

    config = Configuration()
    available_kpis = config.get_available_kpis()
    current_kpis = config.get_selected_kpis()

    labels = [available_kpis.get(k, k) for k in current_kpis]
    kpi_text = ", ".join(labels)

    menu_button(
        label="Afficher la météo",
        description=f"KPIs actuels : {kpi_text}",
        icon="🌤️",
        mode="weather",
        button_text="Lancer la sélection station avec KPI listés"
    )

    menu_button(
        label="Personnaliser les KPIs",
        description="Choisissez les KPIs que vous souhaitez afficher.",
        icon="📊",
        mode="custom",
        button_text="Accéder à la personnalisation des indicateurs"
    )

    menu_button(
        label="Mode administrateur",
        description="Gérez les stations météo (ajout, suppression, modification).",
        icon="⚙️",
        mode="admin",
        button_text="Accéder au menu administrateur"
    )

    menu_button(
        label="Quitter l’application",
        description="Fermer l'application météo.",
        icon="❌",
        mode="exit",
        button_text="Quitter"
    )