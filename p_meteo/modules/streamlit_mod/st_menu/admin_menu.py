import streamlit as st

from modules.configuration import Configuration
from modules.streamlit_mod.st_admin.st_station_admin import StStationAdmin
from modules.streamlit_mod.st_admin.st_station_form import st_station_form


def show_admin():
    """
    Interface Streamlit du mode administrateur.

    Permet :
    - d’afficher les stations existantes
    - d’ajouter une station
    - de modifier une station
    - de supprimer une ou plusieurs stations

    Toute la logique métier est déléguée à StStationAdmin.
    """
    st.subheader("⚙️ Mode administrateur – Stations météo")

    # ---------------------------------------------------------
    # Chargement config + CSV
    # ---------------------------------------------------------
    config = Configuration()
    csv_path = config.get_value("csv_path")

    admin = StStationAdmin(csv_path)
    stations_df = admin.df  # DataFrame actuel

    # ---------------------------------------------------------
    # AFFICHAGE DES STATIONS
    # ---------------------------------------------------------
    if stations_df.empty:
        st.info("Aucune station enregistrée pour le moment.")
    else:
        st.markdown("### 📋 Stations existantes")
        st.dataframe(stations_df, hide_index=True)

    st.markdown("---")

    # ---------------------------------------------------------
    # ONGLET AJOUT / MODIF / SUPPRESSION
    # ---------------------------------------------------------
    tab_ajout, tab_modif, tab_suppr = st.tabs([
        "➕ Ajouter",
        "✏️ Modifier",
        "🗑️ Supprimer"
    ])

    # ---------------------------------------------------------
    # AJOUT
    # ---------------------------------------------------------
    with tab_ajout:
        st.markdown("#### ➕ Ajouter une nouvelle station")

        # Message du cycle précédent
        if "admin_add_message" in st.session_state:
            msg, is_success = st.session_state.pop("admin_add_message")
            st.success(msg) if is_success else st.error(msg)

        # Clé unique pour éviter les collisions Streamlit
        form_key = st.session_state.get("admin_add_form_key", 0)

        result = st_station_form(stations_df, form_key=f"add_{form_key}")

        if result:
            ville, dataset_id = result
            success, msg = admin.add(ville, dataset_id)

            # Stockage du message pour affichage après rerun
            st.session_state["admin_add_message"] = (msg, success)

            # Réinitialisation du formulaire
            st.session_state["admin_add_form_key"] = form_key + 1

            st.rerun()

    # ---------------------------------------------------------
    # MODIFICATION
    # ---------------------------------------------------------
    with tab_modif:
        st.markdown("#### ✏️ Modifier une station existante")

        # Message du cycle précédent
        if "admin_edit_message" in st.session_state:
            msg, is_success = st.session_state.pop("admin_edit_message")
            st.success(msg) if is_success else st.error(msg)

        if stations_df.empty:
            st.info("Aucune station à modifier.")
        else:
            options = [
                f"{row['ville']} ({row['dataset_id']})"
                for _, row in stations_df.iterrows()
            ]

            selection = st.selectbox(
                "Choisissez une station :",
                options,
                key="select_modif"
            )

            # Réinitialisation du formulaire si changement de sélection
            if (
                "last_edit_selection" not in st.session_state
                or st.session_state["last_edit_selection"] != selection
            ):
                st.session_state["admin_edit_form_key"] = 0
                st.session_state["last_edit_selection"] = selection

            if selection:
                idx = options.index(selection)
                row = stations_df.iloc[idx]

                form_key = st.session_state.get("admin_edit_form_key", 0)

                result = st_station_form(
                    stations_df,
                    ville_initiale=row["ville"],
                    dataset_initial=row["dataset_id"],
                    form_key=f"edit_{idx}_{form_key}"
                )

                if result:
                    ville_mod, dataset_mod = result
                    success, msg = admin.edit(idx, ville_mod, dataset_mod)

                    st.session_state["admin_edit_message"] = (msg, success)
                    st.session_state["admin_edit_form_key"] = form_key + 1

                    st.rerun()

    # ---------------------------------------------------------
    # SUPPRESSION
    # ---------------------------------------------------------
    with tab_suppr:
        st.markdown("#### 🗑️ Supprimer une ou plusieurs stations")

        # Message du cycle précédent
        if "admin_delete_message" in st.session_state:
            msg, is_success = st.session_state.pop("admin_delete_message")
            st.success(msg) if is_success else st.error(msg)

        if stations_df.empty:
            st.info("Aucune station à supprimer.")
        else:
            options = [
                f"{row['ville']} ({row['dataset_id']})"
                for _, row in stations_df.iterrows()
            ]

            to_delete = st.multiselect(
                "Sélectionnez les stations :",
                options,
                key="delete_select"
            )

            if to_delete and st.button("Confirmer la suppression", key="delete_confirm"):
                indices = [options.index(sel) for sel in to_delete]
                success, msg = admin.delete(indices)

                st.session_state["admin_delete_message"] = (msg, success)
                st.rerun()

    st.markdown("---")

    # ---------------------------------------------------------
    # RETOUR MENU PRINCIPAL
    # ---------------------------------------------------------
    if st.button("🏠 Retour menu principal", key="back_menu"):
        st.session_state["mode"] = "menu"
        st.rerun()