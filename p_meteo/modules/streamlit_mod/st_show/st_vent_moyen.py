import streamlit as st


class St_VentMoyen:
    """
    Viewer Streamlit pour la force moyenne du vent.
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
        Affiche la force moyenne du vent dans Streamlit.
        """
        value = self.record.vent_moyen
        if value is not None:
            st.metric(label="🌬️ Vent moyen", value=f"{value} km/h")
        else:
            st.warning("Vent moyen non disponible.")

    def get_value(self) -> tuple[str, str]:
        """
        Retourne le label et la valeur du vent moyen.
        """
        value = self.record.vent_moyen
        if value is not None:
            return "🌬️ Vent moyen", f"{value} km/h"
        return "🌬️ Vent moyen", "N/A"