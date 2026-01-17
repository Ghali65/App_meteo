"""
Module d'appel à l'API Toulouse Métropole pour récupérer les données météo.
"""

from typing import Optional
import requests

from p_meteo.modules.configuration import Configuration


class CallApi:
    """Interroge l'API Toulouse Métropole pour un dataset_id donné."""

    def __init__(self, dataset_id: str) -> None:
        self.dataset_id = dataset_id
        self.data: Optional[dict] = None

        config = Configuration()
        self.base_url: str = config.get_value("url")

    def fetch(self) -> None:
        """Récupère les données JSON les plus récentes pour la station."""
        url = (
            f"{self.base_url}{self.dataset_id}/records?"
            "order_by=heure_de_paris%20DESC&limit=1"
        )

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            self.data = response.json()

        except requests.RequestException as error:
            print(f"\n❌ Erreur API pour {self.dataset_id} : {error}")
            print(f"URL appelée : {url}")
            self.data = None
