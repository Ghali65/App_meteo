"""
Point d’entrée de la version Streamlit de l’application météo.
Gère la navigation, l’état de session et déclenche le pipeline météo.
"""

import streamlit as st
from modules.configuration import Configuration
from modules.streamlit_mod.st_menu.main_menu import show_main_menu
from modules.streamlit_mod.st_menu.weather_menu import show_weather
from modules.streamlit_mod.st_menu.kpi_menu import show_kpi_customization
from modules.streamlit_mod.st_menu.admin_menu import show_admin

def run_app():
    """ Point d'entrée de l'application Streamlit. 
    Initialise la session et affiche l'écran correspondant au mode actif. 
    """
    config = Configuration()

    if "initialized" not in st.session_state:
        config.set_selected_kpis(config.get_default_kpis())
        st.session_state["initialized"] = True

    # Initialisation de la session
    if "mode" not in st.session_state:
        st.session_state["mode"] = "menu"

    mode = st.session_state["mode"]

    # Affichage du menu principal
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
