import streamlit as st

class St_DirectionVentMoyen:
    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        if self.record.direction_vent_moyen is not None:
            st.metric(label="🧭 Vent moyen (°)", value=f"{self.record.direction_vent_moyen}°")
        else:
            st.warning("Direction vent moyen non disponible.")

    def get_value(self) -> tuple[str, str]:
        if self.record.direction_vent_moyen is not None:
            return "🧭 Vent moyen (°)", f"{self.record.direction_vent_moyen}°"
        return "🧭 Vent moyen (°)", "N/A"
