import streamlit as st


class St_Pluie:
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