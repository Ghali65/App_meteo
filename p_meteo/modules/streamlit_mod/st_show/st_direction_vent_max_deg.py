import streamlit as st

class St_DirectionVentMaxDeg:
    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        if self.record.direction_vent_max_deg is not None:
            st.metric(label="🧭 Vent max (°)", value=f"{self.record.direction_vent_max_deg}°")
        else:
            st.warning("Direction vent max (°) non disponible.")

    def get_value(self) -> tuple[str, str]:
        if self.record.direction_vent_max_deg is not None:
            return "🧭 Vent max (°)", f"{self.record.direction_vent_max_deg}°"
        return "🧭 Vent max (°)", "N/A"
