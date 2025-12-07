import streamlit as st
from modules.transform.t_ville import TVille


class St_Ville:
    def __init__(self, transform: TVille) -> None:
        self.ville: str | None = transform.ville()

    def display(self) -> None:
        if self.ville:
            st.write(f"🏙️ Ville : **{self.ville}**")
        else:
            st.warning("Ville non disponible.")
