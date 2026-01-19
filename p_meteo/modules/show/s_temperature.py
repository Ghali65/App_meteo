"""
Viewer console pour la température en degrés Celsius.
"""

class STemperature:
    """
    Classe Viewer console pour la température en degrés Celsius.
    """

    def __init__(self, record) -> None:
        """
        Args:
            record: Données météo transformées.
        """
        self.record = record

    def display(self) -> None:
        """Affiche la température"""
        print("🌡️ Température :", self.record.temperature)
