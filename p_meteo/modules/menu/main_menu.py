import os
import json

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def load_config():
    with open("p_meteo/config.json", "r", encoding="utf-8") as f:
        return json.load(f)


def main_menu():
    """
    Menu principal de l'application console.
    """
    while True:
        clear_console()
        config = load_config()

        default_kpis = config.get("default_kpis", [])
        selected_kpis = config.get("selected_kpis", default_kpis)

        print("===========================================")
        print("        🌤️  APPLICATION METEO  🌤️")
        print("===========================================\n")

        print("Veuillez choisir une option :\n")

        print("1) Afficher la météo")
        print("   → Utilise les KPIs par défaut :")
        for kpi in selected_kpis:
            print(f"     - {kpi}")

        print("\n2) Sélectionner les KPIs à afficher")
        print("   → Choisissez parmi tous les KPIs disponibles")

        print("\n3) Mode administrateur")
        print("   → Ajouter une station météo")
        print("   → Gérer les données locales")

        print("\n4) Quitter l'application\n")

        choix = input("Votre choix : ").strip()

        if choix == "1":
            return "show_weather"   # Le main saura quoi faire
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
