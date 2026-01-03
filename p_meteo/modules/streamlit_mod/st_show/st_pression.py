import streamlit as st
from modules.transform.t_pression import TPression

class St_Pression:
    def __init__(self, record: TPression) -> None:
        self.record = record

    def display(self) -> None:
        if self.record.pression is not None:
            st.metric(label="🌬️ Pression", value=f"{self.record.pression} hPa")
        else:
            st.warning("Pression non disponible.")

    def get_value(self) -> tuple[str, str]:
        if self.record.pression is not None:
            return "🌬️ Pression", f"{self.record.pression} hPa"
        return "🌬️ Pression", "N/A"