import streamlit as st

class St_StationId:
    def __init__(self, record) -> None:
        self.record: str | None = record

    def display(self) -> None:
        if self.record.station_id:
            st.write(f"🛰️ Station ID : `{self.record.station_id}`")
        else:
            st.warning("Station ID non disponible.")
