import streamlit as st
from modules.transform.t_pression import TPression


class St_Pression:
    def __init__(self, transform: TPression) -> None:
        self.pression: float | None = transform.pression()

    def display(self) -> None:
        if self.pression is not None:
            st.metric(label="🌬️ Pression", value=f"{self.pression} hPa")
        else:
            st.warning("Pression non disponible.")
