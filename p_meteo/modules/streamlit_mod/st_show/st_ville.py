"""
Viewer Streamlit pour le nom de la ville associée à une station météo.

Ce module fournit un composant utilisé dans la LinkedList Streamlit
pour afficher le KPI `ville` :
- via display() sous forme de texte enrichi
- via get_value() sous forme de couple (label, valeur) pour tableaux ou exports.

La logique métier reste dans Record ; ce viewer ne gère que la présentation.
"""

import streamlit as st


class StVille:
    """
    Viewer Streamlit pour le nom de la ville associée à la station météo.
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
        Affiche le nom de la ville dans Streamlit.
        """
        value = self.record.ville
        if value:
            st.write(f"🏙️ Ville : **{value}**")
        else:
            st.warning("Ville non disponible.")

    def get_value(self) -> tuple[str, str]:
        """
        Retourne le label et le nom de la ville.
        """
        value = self.record.ville
        if value:
            return "🏙️ Ville", str(value)
        return "🏙️ Ville", "N/A"
