class ShowInfo:
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

    def display_humidite(self) -> None:
        print("💧 Humidité :", self.record.humidite())

    def display_pression(self) -> None:
        print("📊 Pression :", self.record.pression())

    def display_temperature(self) -> None:
        print("🌡️ Température :", self.record.temperature())

    def display_heure_maj(self) -> None:
        print("🕒 Dernière mise à jour :", self.record.heure_maj())

    def display_ville(self) -> None:
        print("🏙️ Ville :", self.record.ville())

    def station_id(self) -> None:
        print("🆔 Station :", self.record.station_id())

    def display_all(self) -> None:
        """
        Affiche toutes les informations disponibles.
        """
        print("\n--- Informations météo extraites ---")
        self.display_ville()
        self.station_id()
        self.display_temperature()
        self.display_humidite()
        self.display_pression()
        self.display_heure_maj()
