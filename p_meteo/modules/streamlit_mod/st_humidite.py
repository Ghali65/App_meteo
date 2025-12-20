import streamlit as st
from modules.transform.t_humidite import THumidite


class St_Humidite:
    def __init__(self, record: THumidite) -> None:
        self.record: float | None = record

    def display(self) -> None:
        if self.record.humidite is not None:
            st.metric(label="💧 Humidité", value=f"{self.record.humidite} %")
        else:
            st.warning("Humidité non disponible.")
