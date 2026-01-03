import streamlit as st

class St_VentMoyen:
    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        if self.record.vent_moyen is not None:
            st.metric(label="🌬️ Vent moyen", value=f"{self.record.vent_moyen} km/h")
        else:
            st.warning("Vent moyen non disponible.")

    def get_value(self) -> tuple[str, str]:
        if self.record.vent_moyen is not None:
            return "🌬️ Vent moyen", f"{self.record.vent_moyen} km/h"
        return "🌬️ Vent moyen", "N/A"
