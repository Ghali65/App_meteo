import streamlit as st

class St_Humidite:
    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        if self.record.humidite is not None:
            st.metric(label="💧 Humidité", value=f"{self.record.humidite} %")
        else:
            st.warning("Humidité non disponible.")

    def get_value(self) -> tuple[str, str]:
        if self.record.humidite is not None:
            return "💧 Humidité", f"{self.record.humidite} %"
        return "💧 Humidité", "N/A"
