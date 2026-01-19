"""
Viewer console pour le nom de la ville associée à la station météo.
"""

class SVille:
    """
    Classe Viewer console pour le nom de la ville associée à la station météo.
    """

    def __init__(self, record) -> None:
        """
        Args:
            record: Données météo transformées.
        """
        self.record = record

    def display(self) -> None:
        """Affiche la ville"""
        print("🏙️ Ville :", self.record.ville)
