from ..configuration import Configuration
from ..viewer_factory import ViewerFactory
from ..chained.linked_list import Link, LinkedList

def build_viewer_list(record, selected_kpis) -> LinkedList:
    """
    Construit la liste chaînée des viewers météo
    en utilisant la liste de KPIs passée par main().
    """

    if not selected_kpis:
        raise ValueError("Aucun KPI sélectionné")

    # Premier viewer
    first_viewer = ViewerFactory.create(selected_kpis[0], record)
    linked_list = LinkedList(Link(first_viewer))

    # Viewers suivants
    for kpi_name in selected_kpis[1:]:
        viewer = ViewerFactory.create(kpi_name, record)
        linked_list.ajouter_maillon(Link(viewer))

    return linked_list
