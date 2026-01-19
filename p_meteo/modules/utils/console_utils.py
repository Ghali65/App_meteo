"""
Fonction utilitaire pour nettoyer la console.

Ce module fournit clear_console(), une fonction compatible Windows,
Linux et macOS, qui exécute la commande système appropriée pour
effacer l’affichage du terminal.
"""

import os


def clear_console() -> None:
    """
    Efface la console de manière compatible Windows / Linux / macOS.

    Utilise :
    - 'cls' sous Windows
    - 'clear' sous Linux / macOS
    """
    os.system("cls" if os.name == "nt" else "clear")
