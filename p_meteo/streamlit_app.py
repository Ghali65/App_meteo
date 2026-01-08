import streamlit as st
from modules.configuration import Configuration
from modules.streamlit_mod.st_menu.main_menu import show_main_menu
from modules.streamlit_mod.st_menu.weather_menu import show_weather
from modules.streamlit_mod.st_menu.kpi_menu import show_kpi_customization
from modules.streamlit_mod.st_menu.admin_menu import show_admin

def run_app():
    config = Configuration()

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
