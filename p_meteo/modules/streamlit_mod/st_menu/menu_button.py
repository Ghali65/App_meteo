import streamlit as st

# Couleur unique pour tous les boutons
BUTTON_COLOR = "#2196F3"
BUTTON_HOVER = "#5F8CB9"

def menu_button(label, description, icon, mode, button_text):
    # Bloc visuel + bouton collé
    st.markdown(f"""
        <div style='
            padding: 16px;
            border: 1px solid #ddd;
            border-radius: 12px;
            background-color: #f7f9fc;
        '>
            <div style='font-size: 20px; font-weight: bold; margin-bottom: 6px;'>
                {icon} {label}
            </div>
            <div style='font-size: 14px; color: #555; margin-bottom: 8px;'>
                {description}
            </div>
    """, unsafe_allow_html=True)

    # CSS global pour les boutons
    st.markdown(f"""
        <style>
        div[data-testid="stButton"] > button {{
            background-color: {BUTTON_COLOR};
            color: white;
            width: 100%;
            height: 48px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }}
        div[data-testid="stButton"] > button:hover {{
            background-color: {BUTTON_HOVER};
        }}
        </style>
    """, unsafe_allow_html=True)

    # Bouton cliquable
    if st.button(button_text, key=f"btn_{mode}", use_container_width=True):
        st.session_state["mode"] = mode
        st.rerun()

    # Espacement entre blocs
    st.markdown("</div><div style='height: 16px;'></div>", unsafe_allow_html=True)