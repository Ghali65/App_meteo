class SPluie:
    """
    Viewer console pour la quantité de pluie.
    """

    def __init__(self, record) -> None:
        """
        Args:
            record: Données météo transformées.
        """
        self.record = record

    def display(self) -> None:
        print("🌧️ Pluie :", self.record.pluie)