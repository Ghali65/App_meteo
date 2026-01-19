"""
Viewer console pour la direction du vent maximal.
"""

class SDirectionVentMax:
    """
    Classe Viewer console pour la direction du vent maximal.
    """

    def __init__(self, record) -> None:
        """
        Args:
            record: Données météo transformées.
        """
        self.record = record

    def display(self) -> None:
        """Affiche la direction du vent maximal."""
        print("🧭 Direction vent max :", self.record.direction_vent_max)
