import streamlit as st
from modules.transform.t_humidite import THumidite


class St_Humidite:
    def __init__(self, transform: THumidite) -> None:
        self.humidite: float | None = transform.humidite()

    def display(self) -> None:
        if self.humidite is not None:
            st.metric(label="💧 Humidité", value=f"{self.humidite} %")
        else:
            st.warning("Humidité non disponible.")
