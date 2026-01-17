import streamlit as st


class St_DirectionVentMaxDeg:
    """
    Viewer Streamlit pour la direction du vent maximal en degrés.

    Pattern :
    - reçoit un objet Record
    - expose display() pour l’affichage Streamlit
    - expose get_value() pour les tableaux / exports
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
        Affiche la direction du vent maximal en degrés dans Streamlit.
        """
        value = self.record.direction_vent_max_deg
        if value is not None:
            st.metric(label="🧭 Vent max (°)", value=f"{value}°")
        else:
            st.warning("Direction vent max (°) non disponible.")

    def get_value(self) -> tuple[str, str]:
        """
        Retourne le label et la valeur de la direction du vent max (°).
        """
        value = self.record.direction_vent_max_deg
        if value is not None:
            return "🧭 Vent max (°)", f"{value}°"
        return "🧭 Vent max (°)", "N/A"