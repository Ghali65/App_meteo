import os
from ..configuration import Configuration

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def run_kpi_selection_menu():
    clear_console()
    config = Configuration()

    # Liste complète des KPIs disponibles
    all_kpis = list(config.get_available_kpis().keys())

    print("===========================================")
    print("     🔧  CONFIGURATION DES KPIs METEO")
    print("===========================================\n")

    print("Voici les KPIs disponibles :\n")
    for i, kpi in enumerate(all_kpis, start=1):
        print(f"{i}) {kpi}")

    print("\nSélectionnez les KPIs à afficher (ex: 1,4,5) :")
    choix = input("> ").strip()

    # Extraction des indices valides
    indices = [int(i) for i in choix.split(",") if i.strip().isdigit()]
    new_selection = [all_kpis[i - 1] for i in indices if 1 <= i <= len(all_kpis)]

    if not new_selection:
        print("\n❌ Aucun KPI valide sélectionné.")
        input("\nAppuyez sur Entrée pour continuer.")
        return None  # IMPORTANT : on retourne None si rien n'est sélectionné

    # On retourne simplement la liste des KPIs sélectionnés
    print("\n✅ KPIs sélectionnés :")
    for kpi in new_selection:
        print(f" - {kpi}")

    input("\nAppuyez sur Entrée pour continuer.")
    return new_selection
