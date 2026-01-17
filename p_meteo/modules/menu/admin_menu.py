"""
Menu administrateur permettant de gérer les stations météo.

Ce module affiche un menu console permettant :
- d’ajouter une station
- de supprimer une station
- de modifier une station

Il s’appuie sur :
- Configuration : pour récupérer le chemin du CSV
- StationAdmin : pour exécuter les opérations CRUD
- safe_input_back_or_choice : pour sécuriser les entrées utilisateur
"""

from ..configuration import Configuration
from ..utils.console_utils import clear_console
from ..utils.input_utils import safe_input_back_or_choice
from ..admin.station_admin import StationAdmin


def run_admin_menu() -> None:
    """
    Affiche le menu administrateur et gère les actions associées.

    Fonctionnement :
    - Récupère le chemin du CSV via Configuration
    - Instancie StationAdmin pour gérer les opérations
    - Affiche un menu en boucle jusqu'au retour utilisateur
    """
    config = Configuration()
    csv_path = config.get_value("csv_path")
    admin = StationAdmin(csv_path)

    while True:
        clear_console()
        print("===========================================")
        print("        🛠️  MODE ADMIN - STATIONS")
        print("===========================================\n")

        print("1) Ajouter une nouvelle station")
        print("2) Supprimer une station")
        print("3) Modifier une station\n")
        print("0) ⬅️  Retour au menu principal")

        # safe_input_back_or_choice :
        # - sécurise l'entrée utilisateur
        # - renvoie None si l'utilisateur choisit '0'
        choix = safe_input_back_or_choice(
            "Votre choix : ",
            valid_choices=["1", "2", "3"],
            back_value="0",
            cast_to_int=True
        )

        if choix is None:  # utilisateur a choisi 0 → retour au menu principal
            return

        if choix == 1:
            admin.add()
        elif choix == 2:
            admin.delete()
        elif choix == 3:
            admin.edit()