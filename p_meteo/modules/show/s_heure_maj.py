class SHeureMaj:
    """
    Viewer console pour l’heure de dernière mise à jour des données météo.
    """

    def __init__(self, record) -> None:
        """
        Args:
            record: Instance contenant les données météo.
        """
        self.record = record

    def display(self) -> None:
        print("🕒 Dernière mise à jour :", self.record.heure_maj)