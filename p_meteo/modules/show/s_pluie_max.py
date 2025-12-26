class SPluieMax:
    """
    Affiche l'intensité maximale de pluie.
    """

    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        print("🌧️💦 Pluie max :", self.record.pluie_max)
