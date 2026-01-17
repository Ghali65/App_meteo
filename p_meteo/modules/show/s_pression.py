class SPression:
    """
    Viewer console pour la pression atmosphérique.

    Remarque :
    - display est utilisé comme un "pattern décorateur" :
      il enrichit l’affichage en se basant sur Record.
    """

    def __init__(self, record) -> None:
        """
        Args:
            record: Données météo transformées.
        """
        self.record = record

    def display(self) -> None:
        print("📊 Pression :", self.record.pression)