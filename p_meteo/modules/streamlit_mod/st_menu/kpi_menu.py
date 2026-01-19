"""
Interface Streamlit permettant de personnaliser les KPIs affichés.

Ce module propose une page dédiée où l’utilisateur peut :
- sélectionner les KPIs disponibles
- visualiser la sélection en temps réel
- sauvegarder la configuration choisie

La logique métier reste dans Configuration ; ce module gère uniquement l’UI.
"""

import streamlit as st


def show_kpi_customization(config):
    """
    Interface Streamlit pour personnaliser les KPIs affichés.

    Permet :
    - de sélectionner les KPIs disponibles
    - de visualiser la sélection
    - de sauvegarder la configuration
    """
    st.subheader("🎛️ Personnalisation des KPIs")

    available_kpis = config.get_available_kpis()
    all_kpis = list(available_kpis.keys())

    selected_kpis = st.multiselect(
        "Sélectionnez les KPIs à afficher :",
        options=all_kpis,
        default=config.get_default_kpis(),
        format_func=lambda k: available_kpis.get(k, k)
    )

    if not selected_kpis:
        st.warning("Veuillez sélectionner au moins un KPI.")
        st.stop()

    st.markdown("### ✅ KPIs sélectionnés :")
    for kpi in selected_kpis:
        st.write(f"• {available_kpis.get(kpi, kpi)}")

    col1, col2, col3 = st.columns(3)

    if col1.button("🏠 Retour menu principal"):
        st.session_state["mode"] = "menu"
        st.rerun()

    if col2.button("🌤️ Afficher la météo avec ces KPIs"):
        config.set_selected_kpis(selected_kpis)
        st.session_state["mode"] = "weather"
        st.rerun()

    if col3.button("❌ Quitter"):
        st.session_state["mode"] = "exit"
        st.rerun()
