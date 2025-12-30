import pandas as pd
from typing import Optional, Tuple
from ..configuration import Configuration
from ..extract.call_api import CallApi
from ..utils.console_utils import clear_console
from ..utils.input_utils import ask_yes_no, ask_int_in_range
from ..utils.selection_parser import parse_multi_selection


def run_admin_menu() -> None:
    config = Configuration()
    csv_path = config.get_value("csv_path")

    while True:
        clear_console()
        print("===========================================")
        print("        🛠️  MODE ADMIN - STATIONS")
        print("===========================================\n")

        print("1) Ajouter une nouvelle station")
        print("2) Supprimer une station")
        print("3) Modifier une station")
        print("4) Retour au menu principal\n")

        choix = input("> ").strip()

        if choix == "1":
            _add_station(csv_path)
        elif choix == "2":
            _delete_station(csv_path)
        elif choix == "3":
            _edit_station(csv_path)
        elif choix == "4":
            return        

def _station_form(df_csv: pd.DataFrame, ville_initiale: Optional[str] = None, dataset_initial: Optional[str] = None) -> Optional[Tuple[str, str]]:
    """
    Formulaire commun pour ajouter ou modifier une station.
    Retourne (ville, dataset_id) ou None si annulé.
    """

    clear_console()
    print("=== FORMULAIRE STATION ===\n")

    villes = df_csv["ville"].unique().tolist()

    # --- Sélection ou modification de la ville ---
    print("Sélectionnez une ville :\n")
    for i, ville in enumerate(villes, start=1):
        print(f"{i}) {ville}")
    print(f"{len(villes) + 1}) ➕ Ajouter une nouvelle ville")

    if ville_initiale:
        print(f"\nVille actuelle : {ville_initiale}")

    choix = ask_int_in_range("\nVotre choix : ", 1, len(villes) + 1)

    if choix == len(villes) + 1:
        ville = input("Entrez le nom de la nouvelle ville : ").strip()
        while not ville:
            print("❌ Ville invalide.")
            ville = input("Entrez le nom de la nouvelle ville : ").strip()
    else:
        ville = villes[choix - 1]

    # --- Dataset ID ---
    if dataset_initial:
        print(f"\nDataset ID actuel : {dataset_initial}")

    dataset_id = input("\nEntrez le dataset_id de la station : ").strip()
    while not dataset_id:
        print("❌ dataset_id vide.")
        dataset_id = input("Entrez le dataset_id de la station : ").strip()

    # --- Récapitulatif ---
    print("\n=== RÉCAPITULATIF ===")
    print(f"Ville : {ville}")
    print(f"Dataset ID : {dataset_id}")

    if not ask_yes_no("\nConfirmer ? (O/N) : "):
        print("\n❌ Annulé.")
        input("Appuyez sur Entrée pour continuer.")
        return None

    # --- Test API optionnel ---
    api_ok = False
    if ask_yes_no("\nVoulez-vous tester la station via l'API ? (O/N) : "):
        print("\n🔍 Test de la station via l'API...")

        api = CallApi(dataset_id)
        api.fetch()

        if api.data:
            print("\n✔️ Station reconnue par l'API !")
            api_ok = True
        else:
            print("\n⚠️ Station non reconnue par l'API.")

    if not api_ok:
        if not ask_yes_no("\nVoulez-vous quand même continuer ? (O/N) : "):
            print("\n❌ Annulé.")
            input("Appuyez sur Entrée pour continuer.")
            return None

    return ville, dataset_id

def _add_station(csv_path: str) -> None:
    df = pd.read_csv(csv_path)

    result = _station_form(df)
    if not result:
        return

    ville, dataset_id = result

    if dataset_id in df["dataset_id"].values:
        print("\n⚠️ Cette station existe déjà.")
        input("Appuyez sur Entrée pour continuer.")
        return

    with open(csv_path, "a", encoding="utf-8") as f:
        f.write(f"{dataset_id},{ville}\n")

    print("\n✔️ Station ajoutée avec succès !")
    input("\nAppuyez sur Entrée pour continuer.")

def _edit_station(csv_path: str) -> None:
    clear_console()
    print("=== MODIFICATION DE STATION ===\n")

    df = pd.read_csv(csv_path)

    if df.empty:
        print("⚠️ Aucune station enregistrée.")
        input("\nAppuyez sur Entrée pour continuer.")
        return

    # --- Affichage ---
    print("Stations disponibles :\n")
    for i, row in df.iterrows():
        print(f"{i + 1}) {row['ville']}  →  {row['dataset_id']}")

    print("\n0) ⬅️ Retour")

    choix = ask_int_in_range("\nVotre choix : ", 0, len(df))

    if choix == 0:
        return

    idx = choix - 1
    ville_actuelle = df.iloc[idx]["ville"]
    dataset_actuel = df.iloc[idx]["dataset_id"]

    # --- Formulaire pré-rempli ---
    result = _station_form(df, ville_actuelle, dataset_actuel)
    if not result:
        return

    nouvelle_ville, nouveau_dataset = result

    # --- Mise à jour ---
    df.at[idx, "ville"] = nouvelle_ville
    df.at[idx, "dataset_id"] = nouveau_dataset
    df.to_csv(csv_path, index=False)

    print("\n✔️ Station modifiée avec succès !")
    input("\nAppuyez sur Entrée pour continuer.")

def _delete_station(csv_path: str) -> None:
    """
    Supprime une ou plusieurs stations du CSV via sélection multiple,
    avec possibilité de revenir en arrière.
    """
    clear_console()
    print("=== SUPPRESSION DE STATION ===\n")

    df = pd.read_csv(csv_path)

    if df.empty:
        print("⚠️ Aucune station enregistrée.")
        input("\nAppuyez sur Entrée pour continuer.")
        return

    # --- Affichage indexé ---
    print("Stations disponibles :\n")
    for i, row in df.iterrows():
        print(f"{i + 1}) {row['ville']}  →  {row['dataset_id']}")

    print("\n0) ⬅️  Retour au menu admin")

    max_index = len(df)

    # --- Sélection multiple ---
    print("\nSélectionnez les stations à supprimer (ex : 1,3-5) :")
    print("Ou tapez 0 pour revenir en arrière.\n")

    while True:
        selection = input("> ").strip()

        # Option retour
        if selection == "0":
            print("\nRetour au menu admin.")
            input("Appuyez sur Entrée pour continuer.")
            return

        indices = parse_multi_selection(selection, max_index)

        if indices:
            break

        print(
            f"\n❌ Entrée non valide. Utilisez des entiers entre 1 et {max_index}, "
            "séparés par des virgules ou des plages avec '-'.\n"
            "Tapez 0 pour revenir en arrière.\n"
        )

    # --- Récapitulatif ---
    print("\nVous allez supprimer :\n")
    for idx in indices:
        row = df.iloc[idx - 1]
        print(f" - {row['ville']} ({row['dataset_id']})")

    if not ask_yes_no("\nConfirmer la suppression ? (O/N) : "):
        print("\n❌ Suppression annulée.")
        input("Appuyez sur Entrée pour continuer.")
        return

    # --- Suppression ---
    df = df.drop(df.index[[i - 1 for i in indices]])
    df.to_csv(csv_path, index=False)

    print("\n✔️ Suppression effectuée avec succès !")
    input("\nAppuyez sur Entrée pour continuer.")

