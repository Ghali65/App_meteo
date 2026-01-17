import streamlit as st


class St_Pression:
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