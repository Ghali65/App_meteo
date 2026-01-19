"""
Viewer Streamlit pour la direction maximale du vent.

Ce module définit un viewer utilisé dans la version Streamlit
pour afficher le KPI `direction_vent_max` :
- soit sous forme de métrique (méthode display)
- soit sous forme de couple (label, valeur) pour les tableaux ou listes.

La logique métier reste dans Record ; ce viewer ne fait qu’exposer la donnée.
"""

import streamlit as st


class StDirectionVentMax:
    """
    Viewer Streamlit pour la direction maximale du vent.
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
        Affiche la direction maximale du vent dans Streamlit.
        """
        value = self.record.direction_vent_max
        if value is not None:
            st.metric(label="🧭 Direction vent max", value=str(value))
        else:
            st.warning("Direction vent max non disponible.")

    def get_value(self) -> tuple[str, str]:
        """
        Retourne le label et la valeur de la direction du vent max.
        """
        value = self.record.direction_vent_max
        if value is not None:
            return "🧭 Direction vent max", str(value)
        return "🧭 Direction vent max", "N/A"
