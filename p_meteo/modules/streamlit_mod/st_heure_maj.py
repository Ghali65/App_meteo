import streamlit as st
from modules.transform.t_heure_maj import THeureMaj


class St_HeureMaj:
    def __init__(self, record: THeureMaj) -> None:
        self.record: str | None = record

    def display(self) -> None:
        if self.record.heure_maj:
            st.write(f"⏰ Dernière mise à jour : **{self.record.heure_maj}**")
        else:
            st.warning("Heure de mise à jour non disponible.")
