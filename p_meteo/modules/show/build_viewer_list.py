from ..viewer_factory import ViewerFactory
from ..chained.linked_list import Link, LinkedList

# Ordre d'affichage
VIEWERS = [
    "ville",
    "station",
    "heure",
    "temperature",
    "humidite",
    "pression"
]

def build_viewer_list(record) -> LinkedList:
    """
    Construit la liste chaînée complète des viewers météo.
    """

    # Premier viewer
    first_viewer = ViewerFactory.create(VIEWERS[0], record)
    linked_list = LinkedList(Link(first_viewer))

    # Viewers suivants
    for viewer_type in VIEWERS[1:]:
        viewer = ViewerFactory.create(viewer_type, record)
        linked_list.ajouter_maillon(Link(viewer))

    return linked_list
