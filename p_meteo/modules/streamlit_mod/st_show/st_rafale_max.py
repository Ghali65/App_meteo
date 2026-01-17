import streamlit as st


class St_RafaleMax:
    """
    Viewer Streamlit pour la rafale maximale enregistrée.
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
        Affiche la rafale maximale dans Streamlit.
        """
        value = self.record.rafale_max
        if value is not None:
            st.metric(label="💨 Rafale max", value=f"{value} km/h")
        else:
            st.warning("Rafale max non disponible.")

    def get_value(self) -> tuple[str, str]:
        """
        Retourne le label et la valeur de la rafale max.
        """
        value = self.record.rafale_max
        if value is not None:
            return "💨 Rafale max", f"{value} km/h"
        return "💨 Rafale max", "N/A"