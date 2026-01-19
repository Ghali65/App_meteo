"""
Viewer console pour la direction moyenne du vent.
"""

class SDirectionVentMoyen:
    """
    Classe Viewer console pour la direction moyenne du vent.
    """

    def __init__(self, record) -> None:
        """
        Args:
            record: Données météo transformées.
        """
        self.record = record

    def display(self) -> None:
        """Affiche la direction du vent moyen"""
        print("🧭➡️ Direction vent moyen :", self.record.direction_vent_moyen)
