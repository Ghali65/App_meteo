"""
Viewer console pour la pression atmosphérique.

Remarque :
- display est utilisé comme un "pattern décorateur" :
    il enrichit l’affichage en se basant sur Record.
"""

class SPression:
    """
    Classe Viewer console pour la pression atmosphérique.

    Remarque :
    - display est utilisé comme un "pattern décorateur" :
      il enrichit l’affichage en se basant sur Record.
    """

    def __init__(self, record) -> None:
        """
        Args:
            record: Données météo transformées.
        """
        self.record = record

    def display(self) -> None:
        """Affiche la pression"""
        print("📊 Pression :", self.record.pression)
