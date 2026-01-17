class SVille:
    """
    Viewer console pour le nom de la ville associée à la station météo.
    """

    def __init__(self, record) -> None:
        """
        Args:
            record: Données météo transformées.
        """
        self.record = record

    def display(self) -> None:
        print("🏙️ Ville :", self.record.ville)