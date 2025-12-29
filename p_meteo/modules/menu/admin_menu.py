import pandas as pd
from typing import List
from ..configuration import Configuration
from ..extract.call_api import CallApi
from ..utils.console_utils import clear_console
from ..utils.input_utils import ask_yes_no, ask_int_in_range


def run_admin_menu() -> None:
    """
    Menu administrateur permettant d'ajouter une nouvelle station météo.
    """
    config = Configuration()
    csv_path = config.get_value("csv_path")

    while True:
        clear_console()
        print("===========================================")
        print("        🛠️  MODE ADMIN - STATIONS")
        print("===========================================\n")

        print("1) Ajouter une nouvelle station")
        print("2) Retour au menu principal\n")

        choix = input("> ").strip()

        if choix == "1":
            _add_station(csv_path)
        elif choix == "2":
            return
        else:
            print("\n❌ Choix invalide.")
            input("Appuyez sur Entrée pour continuer.")


def _add_station(csv_path: str) -> None:
    """
    Ajoute une station dans le CSV après sélection de la ville,
    saisie du dataset_id, confirmation et test API optionnel.
    """
    clear_console()
    print("=== AJOUT D'UNE NOUVELLE STATION ===\n")

    # Chargement du CSV
    df_csv = pd.read_csv(csv_path)
    villes = df_csv["ville"].unique().tolist()

    # --- Sélection de la ville ---
    print("Sélectionnez une ville :\n")
    for i, ville in enumerate(villes, start=1):
        print(f"{i}) {ville}")
    print(f"{len(villes) + 1}) ➕ Ajouter une nouvelle ville")

    choix = ask_int_in_range("\nVotre choix : ", 1, len(villes) + 1)

    if choix == len(villes) + 1:
        ville = input("Entrez le nom de la nouvelle ville : ").strip()
        while not ville:
            print("❌ Ville invalide.")
            ville = input("Entrez le nom de la nouvelle ville : ").strip()
    else:
        ville = villes[choix - 1]

    # --- Saisie du dataset_id ---
    dataset_id = input("\nEntrez le dataset_id de la station : ").strip()
    while not dataset_id:
        print("❌ dataset_id vide.")
        dataset_id = input("Entrez le dataset_id de la station : ").strip()

    # --- Récapitulatif ---
    print("\n=== RÉCAPITULATIF ===")
    print(f"Ville : {ville}")
    print(f"Dataset ID : {dataset_id}")

    if not ask_yes_no("\nConfirmer ? (O/N) : "):
        print("\n❌ Ajout annulé.")
        input("Appuyez sur Entrée pour continuer.")
        return

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

    # --- Si API KO, demander confirmation ---
    if not api_ok:
        if not ask_yes_no("\nVoulez-vous quand même l'ajouter ? (O/N) : "):
            print("\n❌ Ajout annulé.")
            input("Appuyez sur Entrée pour continuer.")
            return

    # --- Vérifier doublon ---
    if dataset_id in df_csv["dataset_id"].values:
        print("\n⚠️ Cette station existe déjà dans le CSV.")
        input("Appuyez sur Entrée pour continuer.")
        return

    # --- Ajout direct dans le CSV (version rapide) ---
    with open(csv_path, "a", encoding="utf-8") as f:
        f.write(f"{dataset_id},{ville}\n")

    print("\n✔️ Station ajoutée avec succès !")
    input("\nAppuyez sur Entrée pour continuer.")
