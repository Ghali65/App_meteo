import streamlit as st


class St_Humidite:
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