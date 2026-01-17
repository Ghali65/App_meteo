"""
Construction de la liste chaînée des viewers Streamlit.

Ce module assemble dynamiquement les viewers Streamlit dans une LinkedList,
en respectant l’ordre des KPIs sélectionnés par l’utilisateur.

Fonctionnement :
- Chaque KPI correspond à un viewer Streamlit (classe St_XXX)
- StreamlitViewerFactory crée les instances à partir du nom technique
- LinkedList permet d’afficher les viewers dans l’ordre choisi
"""

from modules.streamlit_mod.st_viewer_factory import StreamlitViewerFactory
from modules.chained.linked_list import Link, LinkedList


def build_streamlit_viewer_list(record, selected_kpis) -> LinkedList:
    """
    Construit la LinkedList des viewers Streamlit via la Factory.

    Args:
        record (Record): Données météo transformées
        selected_kpis (list[str]): Liste des noms techniques des KPIs

    Returns:
        LinkedList: liste chaînée de viewers Streamlit prêts à être affichés
    """

    if not selected_kpis:
        raise ValueError("Aucun KPI sélectionné pour l'affichage Streamlit.")

    # ------------------------------------------------------------------
    # Premier viewer : initialisation de la LinkedList
    # ------------------------------------------------------------------
    first_viewer = StreamlitViewerFactory.create(selected_kpis[0], record)
    linked_list = LinkedList(Link(first_viewer))

    # ------------------------------------------------------------------
    # Viewers suivants : ajoutés un par un dans la liste chaînée
    # ------------------------------------------------------------------
    for kpi_name in selected_kpis[1:]:
        viewer = StreamlitViewerFactory.create(kpi_name, record)
        linked_list.ajouter_maillon(Link(viewer))

    return linked_list