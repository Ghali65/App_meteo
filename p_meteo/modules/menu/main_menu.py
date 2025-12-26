import os
from ..configuration import Configuration

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def main_menu():
    """
    Menu principal de l'application console.
    """
    while True:
        clear_console()
        config = Configuration()

        # On récupère les KPIs par défaut (noms techniques)
        default_kpis = config.get_value("default_kpis")

        # On récupère les labels lisibles
        available_kpis = config.get_available_kpis()  # dict : {technique: label}

        print("===========================================")
        print("        🌤️  APPLICATION METEO  🌤️")
        print("===========================================\n")

        print("Veuillez choisir une option :\n")

        print("1) Afficher la météo")
        print("   → KPIs utilisés :")
        for kpi in default_kpis:
            label = available_kpis.get(kpi, kpi)
            print(f"     - {label}")

        print("\n2) Sélectionner les KPIs à afficher")
        print("   → Modifier la liste des KPIs utilisés")

        print("\n3) Mode administrateur")
        print("   → Ajouter une station météo")
        print("   → Gérer les données locales")

        print("\n4) Quitter l'application\n")

        choix = input("Votre choix : ").strip()

        if choix == "1":
            return "show_weather"
        elif choix == "2":
            return "select_kpis"
        elif choix == "3":
            return "admin_mode"
        elif choix == "4":
            print("\nAu revoir !")
            exit(0)
        else:
            print("\n❌ Choix invalide. Appuyez sur Entrée pour réessayer.")
            input()
