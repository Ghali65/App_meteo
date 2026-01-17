class SPluieMax:
    """
    Viewer console pour l’intensité maximale de pluie.
    """

    def __init__(self, record) -> None:
        """
        Args:
            record: Données météo transformées.
        """
        self.record = record

    def display(self) -> None:
        print("🌧️💦 Pluie max :", self.record.pluie_max)