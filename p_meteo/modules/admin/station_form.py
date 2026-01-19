"""
Formulaire console pour ajouter ou modifier une station météo.
"""

from typing import Optional, Tuple
import pandas as pd

from ..utils.console_utils import clear_console
from ..utils.input_utils import (
    ask_yes_no,
    safe_input_back_or_choice,
)
from ..extract.call_api import CallApi


def station_form(
    df_csv: pd.DataFrame,
    ville_initiale: Optional[str] = None,
    dataset_initial: Optional[str] = None,
) -> Optional[Tuple[str, str]]:
    """
    Formulaire commun pour ajouter ou modifier une station.

    Retourne :
        (ville, dataset_id)
        ou None si annulé ou retour utilisateur.
    """
    clear_console()
    print("=== FORMULAIRE STATION ===\n")

    villes = df_csv["ville"].unique().tolist()

    print("Sélectionnez une ville :\n")
    for i, ville in enumerate(villes, start=1):
        print(f"{i}) {ville}")
    print(f"{len(villes) + 1}) ➕ Ajouter une nouvelle ville\n")
    print("0) ⬅️ Retour")

    if ville_initiale:
        print(f"\nVille actuelle : {ville_initiale}")

    valid_choices = [str(i) for i in range(1, len(villes) + 2)]

    choix = safe_input_back_or_choice(
        "\nVotre choix : ",
        valid_choices=valid_choices,
        back_value="0",
        cast_to_int=True,
    )

    if choix is None:
        return None

    if choix == len(villes) + 1:
        ville = input("Entrez le nom de la nouvelle ville : ").strip()
        while not ville:
            print("❌ Ville invalide.")
            ville = input("Entrez le nom de la nouvelle ville : ").strip()
    else:
        ville = villes[choix - 1]

    if dataset_initial:
        print(f"\nDataset ID actuel : {dataset_initial}")

    dataset_id = input("\nEntrez le dataset_id de la station : ").strip()
    while not dataset_id:
        print("❌ dataset_id vide.")
        dataset_id = input("Entrez le dataset_id de la station : ").strip()

    print("\n=== RÉCAPITULATIF ===")
    print(f"Ville : {ville}")
    print(f"Dataset ID : {dataset_id}")

    if not ask_yes_no("\nConfirmer ? (O/N) : "):
        print("\n❌ Annulé.")
        input("Appuyez sur Entrée pour continuer.")
        return None

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
