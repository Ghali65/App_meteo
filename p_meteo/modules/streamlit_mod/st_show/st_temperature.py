import streamlit as st

class St_Temperature:
    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        if self.record.temperature is not None:
            st.metric(label="🌡️ Température", value=f"{self.record.temperature} °C")
        else:
            st.warning("Température non disponible.")

    def get_value(self) -> tuple[str, str]:
        if self.record.temperature is not None:
            return "🌡️ Température", f"{self.record.temperature} °C"
        return "🌡️ Température", "N/A"
