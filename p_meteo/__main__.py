from typing import List
import pandas as pd

# Menu
from .modules.menu.main_menu import main_menu
from .modules.menu.kpi_menu import run_kpi_selection_menu

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
    "direction_vent_moyen": TDirectionVentMoyen
}


def main() -> None:

    configuration = Configuration()
    default_kpis = configuration.get_value("default_kpis")

    selected_kpis = default_kpis[:]   # KPIs actifs au démarrage
    custom_mode = False               # False = on affiche le menu principal

    while True:

        # Affichage du menu principal uniquement si pas en mode custom
        if not custom_mode:
            action = main_menu()

            if action == "show_weather":
                # KPIs par défaut
                selected_kpis = default_kpis[:]
                custom_mode = False

            elif action == "select_kpis":
                # Menu de sélection de KPIs
                new_kpis = run_kpi_selection_menu()
                if new_kpis:  # sélection valide
                    selected_kpis = new_kpis
                    custom_mode = True  # on ne repassera plus par le menu principal
                else:
                    # Aucune sélection valide → retour au menu principal
                    custom_mode = False
                    continue

            elif action == "admin_mode":
                run_admin_menu()
                continue

            else:
                print("❌ Action inconnue.")
                continue

        # Lancement du pipeline météo avec les KPIs sélectionnés
        keep_running = run_weather_pipeline(selected_kpis)

        if keep_running == "MENU": 
            custom_mode = False
            continue 
        
        if not keep_running: 
            print("👋 Au revoir !") 
            break

def run_weather_pipeline(selected_kpis):

    configuration = Configuration()
    csv_path: str = configuration.get_value("csv_path")

    # Chargement du CSV
    stations_df = pd.read_csv(csv_path)
    mapping = dict(zip(stations_df["dataset_id"], stations_df["ville"]))

    # Sélection des stations
    selector = StationSelector(csv_path)
    dataset_ids: List[str] = selector.choose()

    # Pipeline pour chaque station
    for dataset_id in dataset_ids:
        print(f"\n=== Traitement de la station {dataset_id} ===")

        # 1) Extraction
        df = ExtractCommand(dataset_id, CallApi, ToDataFrame, mapping).execute()

        # 2) Transformation (selon les KPIs sélectionnés)
        transformers = [
            TRANSFORMER_REGISTRY[kpi_name]()
            for kpi_name in selected_kpis
            if kpi_name in TRANSFORMER_REGISTRY
        ]

        record = TransformCommand(df, transformers).execute()

        # 3) Affichage
        ShowCommand(record, selected_kpis).execute()

    # Pause utilisateur
    print("\nAppuyez sur Entrée pour relancer avec les mêmes KPIs.")
    print("Tapez M pour revenir au menu principal.")
    print("Ou tapez Q pour quitter.")
    action = input("> ").strip().upper()
    print("⏎ Action utilisateur :", action)

    if action == "Q":
        return False  # Quitter l'application

    if action == "M":
        return "MENU"  # Signal spécial pour revenir au menu

    return True  # Relancer avec les mêmes KPIs


if __name__ == "__main__":
    main()

