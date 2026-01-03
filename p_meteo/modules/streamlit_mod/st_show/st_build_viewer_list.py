from modules.streamlit_mod.st_viewer_factory import StreamlitViewerFactory
from modules.chained.linked_list import Link, LinkedList


def build_streamlit_viewer_list(record, selected_kpis) -> LinkedList:
    """
    Construit la LinkedList des viewers Streamlit via la Factory.
    """

    # Premier viewer
    first_viewer = StreamlitViewerFactory.create(selected_kpis[0], record)
    linked_list = LinkedList(Link(first_viewer))

    # Viewers suivants
    for viewer_type in selected_kpis[1:]:
        viewer = StreamlitViewerFactory.create(viewer_type, record)
        linked_list.ajouter_maillon(Link(viewer))

    return linked_list
