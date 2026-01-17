class SHumidite:
    """
    Viewer console pour le taux d’humidité.
    """

    def __init__(self, record) -> None:
        """
        Args:
            record: Données météo transformées.
        """
        self.record = record

    def display(self) -> None:
        print("💧 Humidité :", self.record.humidite)