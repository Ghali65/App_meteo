import streamlit as st
from modules.transform.t_heure_maj import THeureMaj


class St_HeureMaj:
    def __init__(self, transform: THeureMaj) -> None:
        self.heure_maj: str | None = transform.heure_maj()

    def display(self) -> None:
        if self.heure_maj:
            st.write(f"⏰ Dernière mise à jour : **{self.heure_maj}**")
        else:
            st.warning("Heure de mise à jour non disponible.")
