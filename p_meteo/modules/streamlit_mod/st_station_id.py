import streamlit as st
from modules.transform.t_station_id import TStationId


class St_StationId:
    def __init__(self, transform: TStationId) -> None:
        self.station_id: str | None = transform.station_id()

    def display(self) -> None:
        if self.station_id:
            st.write(f"🛰️ Station ID : `{self.station_id}`")
        else:
            st.warning("Station ID non disponible.")
