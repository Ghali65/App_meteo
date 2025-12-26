class SDirectionVentMaxDeg:
    """
    Affiche la direction du vent max en degrés.
    """

    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        print("🧭📐 Direction vent max (°) :", self.record.direction_vent_max_deg)
