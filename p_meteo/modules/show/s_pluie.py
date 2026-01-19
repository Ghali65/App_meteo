"""
Viewer console pour la quantité de pluie.
"""

class SPluie:
    """
    Classe Viewer console pour la quantité de pluie.
    """

    def __init__(self, record) -> None:
        """
        Args:
            record: Données météo transformées.
        """
        self.record = record

    def display(self) -> None:
        """Affiche la quantité de pluie."""
        print("🌧️ Pluie :", self.record.pluie)
