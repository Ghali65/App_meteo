import os


def clear_console() -> None:
    """
    Efface la console de manière compatible Windows / Linux / macOS.

    Utilise :
    - 'cls' sous Windows
    - 'clear' sous Linux / macOS
    """
    os.system("cls" if os.name == "nt" else "clear")