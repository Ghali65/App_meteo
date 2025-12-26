class SVentMoyen:
    """
    Affiche la force moyenne du vent.
    """

    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        print("🍃 Vent moyen :", self.record.vent_moyen)
