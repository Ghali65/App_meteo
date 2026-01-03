from typing import List, Optional
from ..configuration import Configuration
from ..utils.selection_parser import parse_multi_selection
from ..utils.console_utils import clear_console
from ..utils.input_utils import ask_yes_no


def run_kpi_selection_menu() -> Optional[List[str]]:
    """
    Menu de sélection des KPIs.
    Permet une saisie multiple (1,3-5,7), confirmation utilisateur,
    et gestion robuste des erreurs.
    Retourne une liste de noms techniques de KPIs ou None si annulation.
    """
    config = Configuration()
    available_kpis = config.get_available_kpis()
    all_kpis = list(available_kpis.keys())
    max_index = len(all_kpis)

    while True:
        clear_console()

        print("===========================================")
        print("     🔧  CONFIGURATION DES KPIs METEO")
        print("===========================================\n")

        print("Voici les KPIs disponibles :\n")
        for i, kpi in enumerate(all_kpis, start=1):
            label = available_kpis.get(kpi, kpi)
            print(f"{i}) {label}")

        print("\n0) ⬅️  Retour\n")

        # Saisie libre avec retour
        choix = input("Sélectionnez les KPIs (ex: 1,4,6-8) : ").strip()

        if choix=="0":
            return None  # retour

        # Parsing multiple
        indices = parse_multi_selection(choix, max_index)

        if not indices:
            print(
                f"\n❌ Format invalide. Utilisez des nombres entre 1 et {max_index}, "
                "séparés par des virgules ou des plages avec '-'. Exemple : 1,3-5,7"
            )
            input("\nAppuyez sur Entrée pour réessayer.")
            continue

        # Conversion indices → noms techniques
        new_selection = [all_kpis[i - 1] for i in indices]

        # Confirmation
        print("\nVous avez sélectionné :")
        for kpi in new_selection:
            print(f" - {available_kpis.get(kpi, kpi)}")

        if ask_yes_no("\nConfirmer ? (O/N) : "):
            return new_selection

        print("\n🔁 Recommençons la sélection…")
        input("Appuyez sur Entrée pour continuer.")
