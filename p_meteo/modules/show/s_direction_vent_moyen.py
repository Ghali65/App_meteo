class SDirectionVentMoyen:
    """
    Affiche la direction moyenne du vent.
    """

    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        print("🧭➡️ Direction vent moyen :", self.record.direction_vent_moyen)
