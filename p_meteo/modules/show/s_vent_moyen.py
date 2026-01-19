"""
Viewer console pour la force moyenne du vent.
"""

class SVentMoyen:
    """
    Classe Viewer console pour la force moyenne du vent.
    """

    def __init__(self, record) -> None:
        """
        Args:
            record: Données météo transformées.
        """
        self.record = record

    def display(self) -> None:
        """Affiche le vent moyen"""
        print("🍃 Vent moyen :", self.record.vent_moyen)
