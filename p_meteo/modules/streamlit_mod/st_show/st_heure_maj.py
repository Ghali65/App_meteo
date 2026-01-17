import streamlit as st


class St_HeureMaj:
    """
    Viewer Streamlit pour l’heure de dernière mise à jour.
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
        Affiche l’heure de dernière mise à jour dans Streamlit.
        """
        value = self.record.heure_maj
        if value:
            st.write(f"⏰ Dernière mise à jour : **{value}**")
        else:
            st.warning("Heure de mise à jour non disponible.")

    def get_value(self) -> tuple[str, str]:
        """
        Retourne le label et la valeur de l’heure de mise à jour.
        """
        value = self.record.heure_maj
        if value:
            return "⏰ Dernière mise à jour", str(value)
        return "⏰ Dernière mise à jour", "N/A"