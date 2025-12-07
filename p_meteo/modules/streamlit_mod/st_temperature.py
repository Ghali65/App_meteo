import streamlit as st
from modules.transform.t_temperature import TTemperature

class St_Temperature:
    def __init__(self, transform: TTemperature) -> None:
        self.temperature: float | None = transform.temperature()

    def display(self) -> None:
        if self.temperature is not None:
            st.metric(label="🌡️ Température", value=f"{self.temperature} °C")
        else:
            st.warning("Température non disponible.")
