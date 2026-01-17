class SDirectionVentMax:
    """
    Viewer console pour la direction du vent maximal (en points cardinaux).
    """

    def __init__(self, record) -> None:
        """
        Args:
            record: Données météo transformées.
        """
        self.record = record

    def display(self) -> None:
        print("🧭 Direction vent max :", self.record.direction_vent_max)