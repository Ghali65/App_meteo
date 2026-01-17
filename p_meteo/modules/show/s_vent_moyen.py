class SVentMoyen:
    """
    Viewer console pour la force moyenne du vent.
    """

    def __init__(self, record) -> None:
        """
        Args:
            record: Données météo transformées.
        """
        self.record = record

    def display(self) -> None:
        print("🍃 Vent moyen :", self.record.vent_moyen)