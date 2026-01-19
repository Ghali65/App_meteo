"""
Viewer Streamlit pour le taux d’humidité.

Ce module fournit un composant utilisé dans la LinkedList Streamlit
pour afficher le KPI `humidite` :
- via display() sous forme de métrique
- via get_value() sous forme de couple (label, valeur) pour tableaux ou exports.

La logique métier reste dans Record ; ce viewer ne gère que la présentation.
"""

import streamlit as st


class StHumidite:
    """
    Viewer Streamlit pour le taux d’humidité.
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
        Affiche le taux d’humidité dans Streamlit.
        """
        value = self.record.humidite
        if value is not None:
            st.metric(label="💧 Humidité", value=f"{value} %")
        else:
            st.warning("Humidité non disponible.")

    def get_value(self) -> tuple[str, str]:
        """
        Retourne le label et la valeur de l’humidité.
        """
        value = self.record.humidite
        if value is not None:
            return "💧 Humidité", f"{value} %"
        return "💧 Humidité", "N/A"
