class STemperature:
    """
    Viewer console pour la température en degrés Celsius.
    """

    def __init__(self, record) -> None:
        """
        Args:
            record: Données météo transformées.
        """
        self.record = record

    def display(self) -> None:
        print("🌡️ Température :", self.record.temperature)