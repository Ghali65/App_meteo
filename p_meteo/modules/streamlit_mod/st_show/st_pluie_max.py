import streamlit as st

class St_PluieMax:
    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        if self.record.pluie_max is not None:
            st.metric(label="🌧️ Pluie max", value=f"{self.record.pluie_max} mm")
        else:
            st.warning("Pluie max non disponible.")

    def get_value(self) -> tuple[str, str]:
        if self.record.pluie_max is not None:
            return "🌧️ Pluie max", f"{self.record.pluie_max} mm"
        return "🌧️ Pluie max", "N/A"