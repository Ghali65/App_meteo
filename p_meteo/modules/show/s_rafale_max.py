class SRafaleMax:
    """
    Affiche la rafale maximale.
    """

    def __init__(self, record) -> None:
        self.record = record

    def display(self) -> None:
        print("💨 Rafale max :", self.record.rafale_max)
