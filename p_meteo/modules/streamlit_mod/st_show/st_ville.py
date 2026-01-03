import streamlit as st

class St_Ville:
    def __init__(self, record):
        self.record = record

    def display(self):
        if self.record.ville:
            st.write(f"🏙️ Ville : **{self.record.ville}**")
        else:
            st.warning("Ville non disponible.")

    def get_value(self) -> tuple[str, str]:
        if self.record.ville:
            return "🏙️ Ville", str(self.record.ville)
        return "🏙️ Ville", "N/A"