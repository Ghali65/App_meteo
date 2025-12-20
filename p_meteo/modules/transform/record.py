class Record:
    """
    Objet métier contenant toutes les données météo transformées.
    Enrichi progressivement par les classes TXXX.
    """

    def __init__(self):
        self.ville = None
        self.station_id = None
        self.temperature = None
        self.heure_maj = None
        self.humidite = None
        self.pression = None

    # Accesseurs (optionnels mais propres)
    def get_ville(self): return self.ville
    def get_station_id(self): return self.station_id
    def get_temperature(self): return self.temperature
    def get_heure_maj(self): return self.heure_maj
    def get_humidite(self): return self.humidite
    def get_pression(self): return self.pression
