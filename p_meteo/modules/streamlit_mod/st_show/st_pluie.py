import streamlit as st

class St_Pluie:
    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        if self.record.pluie is not None:
            st.metric(label="🌧️ Pluie", value=f"{self.record.pluie} mm")
        else:
            st.warning("Pluie non disponible.")

    def get_value(self) -> tuple[str, str]:
        if self.record.pluie is not None:
            return "🌧️ Pluie", f"{self.record.pluie} mm"
        return "🌧️ Pluie", "N/A"
