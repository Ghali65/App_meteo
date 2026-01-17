class Record:
    """
    Objet métier contenant toutes les données météo transformées.

    Les attributs sont créés dynamiquement en fonction des KPIs définis
    dans le mapping (kpi_mapping). Cela permet :
    - d’ajouter un nouveau KPI sans modifier la classe Record
    - de garder un objet unique qui centralise toutes les valeurs
    """

    def __init__(self, kpi_mapping: dict):
        """
        Initialise un Record avec des champs génériques et des champs dynamiques.

        Args:
            kpi_mapping (dict): mapping nom_technique → champ API
                                utilisé pour créer les attributs dynamiques.
        """
        # Champs génériques toujours présents
        self.ville = None
        self.dataset_id = None
        self.heure_maj = None  # ← IMPORTANT : certains viewers en dépendent

        # Création dynamique des attributs pour chaque KPI
        for kpi_name in kpi_mapping.keys():
            setattr(self, kpi_name, None)

    def __repr__(self) -> str:
        """
        Représentation textuelle du Record, utile pour le debug.
        """
        attrs = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"Record({attrs})"