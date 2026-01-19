"""
Viewer console pour le taux d’humidité.
"""

class SHumidite:
    """
    Classe Viewer console pour le taux d’humidité.
    """

    def __init__(self, record) -> None:
        """
        Args:
            record: Données météo transformées.
        """
        self.record = record

    def display(self) -> None:
        """Affichage taux humidité"""
        print("💧 Humidité :", self.record.humidite)
