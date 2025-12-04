class SHeureMaj:
    """
    Classe utilitaire pour afficher les informations météo extraites d'un objet Record.
    """

    def __init__(self, record) -> None:
        """
        Initialise la classe avec une instance de Record.

        Args:
            record (Record): Instance contenant les données météo.
        """
        self.record = record

    def display(self) -> None:
        print("🕒 Dernière mise à jour :", self.record.heure_maj())

