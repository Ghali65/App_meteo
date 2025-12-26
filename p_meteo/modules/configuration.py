import json
from typing import Any, Dict

class Configuration:
    _instance = None
    _config: Dict[str, Any] = {}
    _config_path: str = "p_meteo/config.json"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Configuration, cls).__new__(cls)
            try:
                with open(cls._config_path, "r", encoding="utf-8") as jsn_config:
                    cls._instance._config = json.load(jsn_config)
            except FileNotFoundError:
                raise FileNotFoundError(f"⚠️ Fichier {cls._config_path} introuvable.")
            except json.JSONDecodeError:
                raise ValueError("⚠️ Fichier config.json invalide (JSON mal formé).")
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
        with open(self._config_path, "w", encoding="utf-8") as jsn_config:
            json.dump(self._config, jsn_config, indent=4, ensure_ascii=False)

    def get_value(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def all(self) -> Dict[str, Any]:
        return self._config

    def save(self) -> None:
        """
        Sauvegarde explicitement la configuration dans config.json.
        Utile lorsque plusieurs modifications sont faites avant écriture.
        """
        with open(self._config_path, "w", encoding="utf-8") as jsn_config:
            json.dump(self._config, jsn_config, indent=4, ensure_ascii=False)

    # ----------------------------------------------------------------------
    # 🔥 Méthodes spécialisées pour ton pipeline
    # ----------------------------------------------------------------------

    def get_selected_kpis(self) -> list[str]:
        """
        Retourne la liste des KPIs sélectionnés (noms techniques).
        Exemple : ["ville", "temperature", "heure"]
        """
        return self._config.get("selected_kpis", [])

    def set_selected_kpis(self, kpis: list[str]) -> None:
        """
        Met à jour la liste des KPIs sélectionnés.
        Ne sauvegarde PAS automatiquement pour laisser le choix à l'appelant.
        """
        self._config["selected_kpis"] = kpis

    def get_default_kpis(self) -> list[str]:
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
        nom_technique → nom de classe viewer
        """
        return self._config.get("viewer_mapping", {})
