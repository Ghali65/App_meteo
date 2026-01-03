import streamlit as st

class St_DirectionVentMax:
    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        if self.record.direction_vent_max is not None:
            st.metric(label="🧭 Direction vent max", value=self.record.direction_vent_max)
        else:
            st.warning("Direction vent max non disponible.")

    def get_value(self) -> tuple[str, str]:
        if self.record.direction_vent_max is not None:
            return "🧭 Direction vent max", str(self.record.direction_vent_max)
        return "🧭 Direction vent max", "N/A"
