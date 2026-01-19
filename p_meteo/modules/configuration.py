"""
Gestion centralisée de la configuration du projet (pattern Singleton).
Charge config.json une seule fois et expose des méthodes utilitaires
pour accéder aux KPIs, mappings et paramètres globaux.
"""

import json
from typing import Any, Dict, List


class Configuration:
    """
    Singleton chargé de lire et gérer config.json.

    - _instance : instance unique du Singleton
    - _config : dictionnaire Python contenant le JSON chargé
    - CONFIG_PATH : chemin du fichier config.json

    Le fichier est chargé une seule fois lors du premier appel.
    """

    _instance = None
    _config: Dict[str, Any] = {}

    # Chemin du fichier JSON de configuration
    CONFIG_PATH: str = "p_meteo/config.json"

    def __new__(cls):
        """
        Pattern Singleton :
        Si aucune instance n'existe, on charge le fichier JSON.
        Sinon, on renvoie l'instance existante.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            try:
                with open(cls.CONFIG_PATH, "r", encoding="utf-8") as jsn_config:
                    cls._instance._config = json.load(jsn_config)

            except FileNotFoundError as exc:
                raise FileNotFoundError(
                    f"⚠️ Fichier {cls.CONFIG_PATH} introuvable."
                    ) from exc

            except json.JSONDecodeError as exc:
                raise ValueError(
                    "⚠️ Fichier config.json invalide (JSON mal formé)."
                    ) from exc

        return cls._instance

    # ----------------------------------------------------------------------
    # 🔧 Méthodes génériques
    # ----------------------------------------------------------------------

    def set_value(self, key: str, value: Any) -> None:
        """
        Ajoute ou met à jour une clé dans la config
        et sauvegarde immédiatement dans le fichier JSON.
        """
        self._config[key] = value
        self.save()

    def get_value(self, key: str, default: Any = None) -> Any:
        """Retourne la valeur associée à une clé, ou une valeur par défaut."""
        return self._config.get(key, default)

    def all(self) -> Dict[str, Any]:
        """Retourne l'intégralité de la configuration sous forme de dict."""
        return self._config

    def save(self) -> None:
        """
        Sauvegarde explicitement la configuration dans config.json.
        Utile lorsque plusieurs modifications sont faites avant écriture.
        """
        with open(self.CONFIG_PATH, "w", encoding="utf-8") as jsn_config:
            json.dump(self._config, jsn_config, indent=4, ensure_ascii=False)

    # ----------------------------------------------------------------------
    # 🔥 Méthodes spécialisées pour ton pipeline
    # ----------------------------------------------------------------------

    def get_selected_kpis(self) -> List[str]:
        """
        Retourne la liste des KPIs sélectionnés (noms techniques).
        Exemple : ["ville", "temperature", "heure"]
        """
        return self._config.get("selected_kpis", [])

    def set_selected_kpis(self, kpis: List[str]) -> None:
        """
        Met à jour la liste des KPIs sélectionnés.
        Ne sauvegarde PAS automatiquement pour laisser le choix à l'appelant.
        """
        self._config["selected_kpis"] = kpis

    def get_default_kpis(self) -> List[str]:
        """
        Retourne la liste des KPIs par défaut (noms techniques).
        """
        return self._config.get("default_kpis", [])

    def get_available_kpis(self) -> Dict[str, str]:
        """
        Retourne le dictionnaire des KPIs disponibles :
        nom_technique → nom_user_friendly
        """
        return self._config.get("available_kpis", {})

    def get_kpi_mapping(self) -> Dict[str, str]:
        """
        Retourne le mapping :
        nom_technique → champ API
        """
        return self._config.get("kpi_mapping", {})

    def get_viewer_mapping(self) -> Dict[str, str]:
        """
        Retourne le mapping :
        nom_technique → nom de classe viewer console
        """
        return self._config.get("viewer_mapping", {})
