"""
Point d'entrée de l'application console P-Météo.
Gère le menu principal et l'exécution du pipeline météo.
"""

from typing import List
import pandas as pd

# Menus
from .modules.menu.main_menu import main_menu
from .modules.menu.kpi_menu import run_kpi_selection_menu
from .modules.menu.admin_menu import run_admin_menu

# Configuration
from .modules.configuration import Configuration

# Extraction
from .modules.extract.station_selector import StationSelector
from .modules.extract.call_api import CallApi
from .modules.extract.to_dataframe import ToDataFrame

# Transformateurs
from .modules.transform.t_ville import TVille
from .modules.transform.t_temperature import TTemperature
from .modules.transform.t_heure_maj import THeureMaj
from .modules.transform.t_humidite import THumidite
from .modules.transform.t_pression import TPression
from .modules.transform.t_pluie import TPluie
from .modules.transform.t_pluie_max import TPluieMax
from .modules.transform.t_vent_moyen import TVentMoyen
from .modules.transform.t_rafale_max import TRafaleMax
from .modules.transform.t_direction_vent_max import TDirectionVentMax
from .modules.transform.t_direction_vent_max_deg import TDirectionVentMaxDeg
from .modules.transform.t_direction_vent_moyen import TDirectionVentMoyen

# Commands
from .modules.command import ExtractCommand, TransformCommand, ShowCommand


# Mapping nom technique → classe transformer
TRANSFORMER_REGISTRY = {
    "ville": TVille,
    "temperature": TTemperature,
    "heure_maj": THeureMaj,
    "humidite": THumidite,
    "pression": TPression,
    "pluie": TPluie,
    "pluie_max": TPluieMax,
    "vent_moyen": TVentMoyen,
    "rafale_max": TRafaleMax,
    "direction_vent_max": TDirectionVentMax,
    "direction_vent_max_deg": TDirectionVentMaxDeg,
    "direction_vent_moyen": TDirectionVentMoyen,
}


def main() -> None:
    """
    Boucle principale de l'application console.
    Gère les menus et déclenche le pipeline météo.
    """
    configuration = Configuration()
    default_kpis = configuration.get_value("default_kpis")

    selected_kpis = default_kpis[:]   # KPIs actifs au démarrage
    custom_mode = False               # False = menu principal visible

    while True:

        if not custom_mode:
            action = main_menu()

            if action == "show_weather":
                selected_kpis = default_kpis[:]
                custom_mode = False

            elif action == "select_kpis":
                new_kpis = run_kpi_selection_menu()
                if new_kpis:
                    selected_kpis = new_kpis
                    custom_mode = True
                else:
                    custom_mode = False
                    continue

            elif action == "admin_mode":
                run_admin_menu()
                continue

        keep_running = run_weather_pipeline(selected_kpis)

        if keep_running is True:
            custom_mode = True
            continue

        if keep_running == "MENU":
            custom_mode = False
            continue

        if keep_running is False:
            print("\n👋 Au revoir !\n")
            break


def run_weather_pipeline(selected_kpis):
    """
    Exécute le pipeline météo complet :
    - sélection des stations
    - extraction
    - transformation
    - affichage
    """
    configuration = Configuration()
    csv_path: str = configuration.get_value("csv_path")

    stations_df = pd.read_csv(csv_path)
    mapping = dict(zip(stations_df["dataset_id"], stations_df["ville"]))

    selector = StationSelector(csv_path)
    dataset_ids: List[str] = selector.choose()

    if dataset_ids is None:
        return "MENU"

    for dataset_id in dataset_ids:
        print(f"\n=== Traitement de la station {dataset_id} ===\n")

        df = ExtractCommand(dataset_id, CallApi, ToDataFrame, mapping).execute()

        transformers = [
            TRANSFORMER_REGISTRY[kpi_name]()
            for kpi_name in selected_kpis
            if kpi_name in TRANSFORMER_REGISTRY
        ]

        record = TransformCommand(df, transformers).execute()

        ShowCommand(record, selected_kpis).execute()

    print("\n=====================================================================")
    print("\nAppuyez sur Entrée pour relancer avec les mêmes KPIs.")
    print("\nTapez M pour revenir au menu principal.")
    print("\nOu tapez Q pour quitter.")
    print("\n=====================================================================\n")

    while True:
        action = input("Votre choix : ").strip().upper()
        print("⏎ Action utilisateur :", action)

        if action == "":
            return True

        if action == "M":
            return "MENU"

        if action == "Q":
            return False

        print("\n❌ Saisie invalide.")
        print("Veuillez taper Entrée, M ou Q.")


if __name__ == "__main__":
    main()
