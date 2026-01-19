"""
Viewer Streamlit pour la pression atmosphérique.

Ce module fournit un composant utilisé dans la LinkedList Streamlit
pour afficher le KPI `pression` :
- via display() sous forme de métrique
- via get_value() sous forme de couple (label, valeur) pour tableaux ou exports.

La logique métier reste dans Record ; ce viewer ne gère que la présentation.
"""

import streamlit as st


class StPression:
    """
    Viewer Streamlit pour la pression atmosphérique.
    """

    def __init__(self, record) -> None:
        """
        Initialise le viewer avec une instance de Record.

        Args:
            record: Données météo transformées.
        """
        self.record = record

    def display(self) -> None:
        """
        Affiche la pression atmosphérique dans Streamlit.
        """
        value = self.record.pression
        if value is not None:
            st.metric(label="🌬️ Pression", value=f"{value} hPa")
        else:
            st.warning("Pression non disponible.")

    def get_value(self) -> tuple[str, str]:
        """
        Retourne le label et la valeur de la pression.
        """
        value = self.record.pression
        if value is not None:
            return "🌬️ Pression", f"{value} hPa"
        return "🌬️ Pression", "N/A"
