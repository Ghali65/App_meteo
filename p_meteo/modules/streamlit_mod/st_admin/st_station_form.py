import streamlit as st
import pandas as pd
from typing import Optional, Tuple
from modules.extract.call_api import CallApi


def st_station_form(
    df_csv: pd.DataFrame,
    ville_initiale: Optional[str] = None,
    dataset_initial: Optional[str] = None,
    form_key: str = "default"
) -> Optional[Tuple[str, str]]:
    """
    Version Streamlit du formulaire station.
    Retourne (ville, dataset_id) ou None si annulé.
    form_key permet d'éviter les collisions d'ID Streamlit.
    """

    st.markdown("### 📝 Formulaire station")

    # ---------------------------------------------------------
    # Sélection ou ajout d'une ville
    # ---------------------------------------------------------
    villes = df_csv["ville"].unique().tolist()
    choix_ville = villes + ["➕ Ajouter une nouvelle ville"]

    index_default = (
        choix_ville.index(ville_initiale)
        if ville_initiale in choix_ville
        else 0
    )

    ville_selection = st.selectbox(
        "Sélectionnez une ville :",
        choix_ville,
        index=index_default,
        key=f"ville_select_{form_key}"
    )

    if ville_selection == "➕ Ajouter une nouvelle ville":
        ville = st.text_input("Nouvelle ville :", value="", key=f"ville_new_{form_key}")
    else:
        ville = ville_selection

    # ---------------------------------------------------------
    # Dataset ID
    # ---------------------------------------------------------
    dataset_id = st.text_input(
        "Dataset ID :",
        value=dataset_initial if dataset_initial else "",
        key=f"dataset_{form_key}"
    )

    # ---------------------------------------------------------
    # Test API optionnel
    # ---------------------------------------------------------
    test_api = st.checkbox(
        "Tester la station via l'API",
        key=f"test_api_{form_key}"
    )

    api_ok = False

    if test_api and dataset_id.strip():
        st.info("🔍 Test de la station via l'API…")
        api = CallApi(dataset_id)
        api.fetch()

        if api.data:
            api_ok = True
            st.success("✔️ Station reconnue par l'API.")
        else:
            st.warning("⚠️ Station non reconnue par l'API.")

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------
    if st.button("Valider", key=f"valider_{form_key}"):
        if not ville.strip():
            st.error("❌ Ville invalide.")
            return None

        if not dataset_id.strip():
            st.error("❌ dataset_id vide.")
            return None

        if test_api and not api_ok:
            st.warning("La station n'a pas été reconnue par l'API.")
            if not st.checkbox("Continuer malgré tout", key=f"force_continue_{form_key}"):
                return None

        return ville.strip(), dataset_id.strip()

    return None