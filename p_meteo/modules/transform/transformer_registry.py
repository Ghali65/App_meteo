"""
Registre central des transformateurs métier.

Ce module rassemble l’ensemble des classes de transformation utilisées
dans le pipeline météo. Chaque clé correspond au nom technique d’un KPI,
et chaque valeur est la classe du transformateur chargé d’enrichir le
Record à partir du DataFrame extrait.

Ce registre permet au TransformCommand de construire dynamiquement la
liste des transformateurs à appliquer selon les KPIs sélectionnés.
"""

from .t_ville import TVille
from .t_temperature import TTemperature
from .t_heure_maj import THeureMaj
from .t_humidite import THumidite
from .t_pression import TPression
from .t_pluie import TPluie
from .t_pluie_max import TPluieMax
from .t_vent_moyen import TVentMoyen
from .t_rafale_max import TRafaleMax
from .t_direction_vent_max import TDirectionVentMax
from .t_direction_vent_max_deg import TDirectionVentMaxDeg
from .t_direction_vent_moyen import TDirectionVentMoyen


TRANSFORMER_REGISTRY = {
    "ville": TVille,
    "temperature": TTemperature,
    "heure_maj": THeureMaj,
    "humidite": THumidite,
    "pression": TPression,
    "pluie": TPluie,
    "pluie_max": TPluieMax,
    "vent_moyen": TVentMoyen,
    "rafale_max": TRafaleMax,
    "direction_vent_max": TDirectionVentMax,
    "direction_vent_max_deg": TDirectionVentMaxDeg,
    "direction_vent_moyen": TDirectionVentMoyen,
}
