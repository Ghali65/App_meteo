import streamlit as st


class St_DirectionVentMoyen:
    """
    Viewer Streamlit pour la direction moyenne du vent.
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
        Affiche la direction moyenne du vent dans Streamlit.
        """
        value = self.record.direction_vent_moyen
        if value is not None:
            st.metric(label="🧭 Vent moyen (°)", value=f"{value}°")
        else:
            st.warning("Direction vent moyen non disponible.")

    def get_value(self) -> tuple[str, str]:
        """
        Retourne le label et la valeur de la direction moyenne du vent.
        """
        value = self.record.direction_vent_moyen
        if value is not None:
            return "🧭 Vent moyen (°)", f"{value}°"
        return "🧭 Vent moyen (°)", "N/A"