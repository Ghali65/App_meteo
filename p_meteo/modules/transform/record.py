class Record:
    """
    Objet métier contenant toutes les données météo transformées.
    Les attributs sont créés dynamiquement en fonction des KPIs.
    """

    def __init__(self, kpi_mapping: dict):
        # Champs génériques
        self.ville = None
        self.dataset_id = None
        self.heure_maj = None  # ← IMPORTANT : viewer en dépend

        # Création dynamique des attributs pour chaque KPI
        for kpi_name in kpi_mapping.keys():
            setattr(self, kpi_name, None)

    def __repr__(self):
        attrs = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"Record({attrs})"
