import streamlit as st

class St_RafaleMax:
    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        if self.record.rafale_max is not None:
            st.metric(label="💨 Rafale max", value=f"{self.record.rafale_max} km/h")
        else:
            st.warning("Rafale max non disponible.")

    def get_value(self) -> tuple[str, str]:
        if self.record.rafale_max is not None:
            return "💨 Rafale max", f"{self.record.rafale_max} km/h"
        return "💨 Rafale max", "N/A"
