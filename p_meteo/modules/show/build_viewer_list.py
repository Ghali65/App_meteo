"""
Construction de la liste chaînée des viewers console.

Ce module assemble dynamiquement les viewers météo dans une LinkedList,
en respectant l’ordre des KPIs sélectionnés par l’utilisateur.

Fonctionnement :
- Chaque KPI correspond à un viewer console (classe SXXX)
- ViewerFactory crée les instances à partir du nom technique
- LinkedList permet d’afficher les viewers dans l’ordre choisi
"""

from ..viewer_factory import ViewerFactory
from ..chained.linked_list import Link, LinkedList


def build_viewer_list(record, selected_kpis) -> LinkedList:
    """
    Construit la liste chaînée des viewers météo
    en utilisant la liste de KPIs passée par main().

    Args:
        record (Record): Données météo transformées
        selected_kpis (list[str]): Liste des noms techniques des KPIs

    Returns:
        LinkedList: liste chaînée de viewers prêts à être affichés

    Raises:
        ValueError: si aucun KPI n’est sélectionné
    """

    if not selected_kpis:
        raise ValueError("Aucun KPI sélectionné")

    # ------------------------------------------------------------------
    # Premier viewer : on initialise la LinkedList avec le premier KPI
    # ------------------------------------------------------------------
    first_viewer = ViewerFactory.create(selected_kpis[0], record)
    linked_list = LinkedList(Link(first_viewer))

    # ------------------------------------------------------------------
    # Viewers suivants : ajoutés un par un dans la liste chaînée
    # ------------------------------------------------------------------
    for kpi_name in selected_kpis[1:]:
        viewer = ViewerFactory.create(kpi_name, record)
        linked_list.append(Link(viewer))


    return linked_list