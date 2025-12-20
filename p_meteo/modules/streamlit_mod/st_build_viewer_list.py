from .st_viewer_factory import StreamlitViewerFactory
from modules.chained.linked_list import Link, LinkedList

VIEWERS = [
    "ville",
    "temperature",
    "heure",
    "humidite",
    "pression"
]

def build_streamlit_viewer_list(record) -> LinkedList:
    """
    Construit la LinkedList des viewers Streamlit via la Factory.
    """

    # Premier viewer
    first_viewer = StreamlitViewerFactory.create(VIEWERS[0], record)
    linked_list = LinkedList(Link(first_viewer))

    # Viewers suivants
    for viewer_type in VIEWERS[1:]:
        viewer = StreamlitViewerFactory.create(viewer_type, record)
        linked_list.ajouter_maillon(Link(viewer))

    return linked_list
