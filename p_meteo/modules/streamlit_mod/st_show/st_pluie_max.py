import streamlit as st


class St_PluieMax:
    """
    Viewer Streamlit pour l’intensité maximale de pluie.
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
        Affiche l’intensité maximale de pluie dans Streamlit.
        """
        value = self.record.pluie_max
        if value is not None:
            st.metric(label="🌧️ Pluie max", value=f"{value} mm")
        else:
            st.warning("Pluie max non disponible.")

    def get_value(self) -> tuple[str, str]:
        """
        Retourne le label et la valeur de la pluie max.
        """
        value = self.record.pluie_max
        if value is not None:
            return "🌧️ Pluie max", f"{value} mm"
        return "🌧️ Pluie max", "N/A"