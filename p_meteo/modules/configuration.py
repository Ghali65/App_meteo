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
