"""
Menu principal de l'application console.

Affiche les différentes options disponibles :
- Afficher la météo (avec les KPIs par défaut)
- Personnaliser les KPIs affichés
- Accéder au mode administrateur
- Quitter l’application

Ce menu constitue le point d’entrée de l’expérience console.
"""

from p_meteo.modules.configuration import Configuration
from p_meteo.modules.utils.input_utils import safe_input_choice
from p_meteo.modules.utils.console_utils import clear_console


def main_menu():
    """
    Affiche le menu principal et retourne l'action choisie.

    Retourne :
        - "show_weather"
        - "select_kpis"
        - "admin_mode"
        - quitte l'application si choix "Q"
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
        print("   → Personnaliser la liste des KPIs affichés")

        print("\n3) Mode administrateur")
        print("   → Ajouter, supprimer ou modifier une station météo")

        print("\nQ) ❌  Quitter l'application\n")

        choix = safe_input_choice("Votre choix : ", ["1", "2", "3", "Q"])

        if choix == "1":
            return "show_weather"
        elif choix == "2":
            return "select_kpis"
        elif choix == "3":
            return "admin_mode"
        elif choix == "Q":
            print("\n👋 Au revoir !\n")
            exit()