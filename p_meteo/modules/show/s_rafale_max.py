"""
Viewer console pour la rafale maximale enregistrée.
"""

class SRafaleMax:
    """
    Classe Viewer console pour la rafale maximale enregistrée.
    """

    def __init__(self, record) -> None:
        """
        Args:
            record: Données météo transformées.
        """
        self.record = record

    def display(self) -> None:
        """Affiche rafale de vent max"""
        print("💨 Rafale max :", self.record.rafale_max)
