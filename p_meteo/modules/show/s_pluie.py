class SPluie:
    """
    Affiche la quantité de pluie.
    """

    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        print("🌧️ Pluie :", self.record.pluie)
