import streamlit as st


class St_Temperature:
    """
    Viewer Streamlit pour la température en degrés Celsius.
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
        Affiche la température dans Streamlit.
        """
        value = self.record.temperature
        if value is not None:
            st.metric(label="🌡️ Température", value=f"{value} °C")
        else:
            st.warning("Température non disponible.")

    def get_value(self) -> tuple[str, str]:
        """
        Retourne le label et la valeur de la température.
        """
        value = self.record.temperature
        if value is not None:
            return "🌡️ Température", f"{value} °C"
        return "🌡️ Température", "N/A"