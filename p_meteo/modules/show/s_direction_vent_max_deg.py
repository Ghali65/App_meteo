class SDirectionVentMaxDeg:
    """
    Viewer console pour la direction du vent maximal en degrés.

    Pattern :
    - reçoit un objet Record
    - expose une méthode display() qui lit un attribut du Record
    """

    def __init__(self, record) -> None:
        """
        Initialise le viewer avec une instance de Record.

        Args:
            record: Données météo transformées.
        """
        self.record = record

    def display(self) -> None:
        print("🧭📐 Direction vent max (°) :", self.record.direction_vent_max_deg)