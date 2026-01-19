"""
Viewer Streamlit pour la quantité de pluie.

Ce module fournit un composant utilisé dans la LinkedList Streamlit
pour afficher le KPI `pluie` :
- via display() sous forme de métrique
- via get_value() sous forme de couple (label, valeur) pour tableaux ou exports.

La logique métier reste dans Record ; ce viewer ne gère que la présentation.
"""

import streamlit as st


class StPluie:
    """
    Viewer Streamlit pour la quantité de pluie.
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
        Affiche la quantité de pluie dans Streamlit.
        """
        value = self.record.pluie
        if value is not None:
            st.metric(label="🌧️ Pluie", value=f"{value} mm")
        else:
            st.warning("Pluie non disponible.")

    def get_value(self) -> tuple[str, str]:
        """
        Retourne le label et la valeur de la pluie.
        """
        value = self.record.pluie
        if value is not None:
            return "🌧️ Pluie", f"{value} mm"
        return "🌧️ Pluie", "N/A"
