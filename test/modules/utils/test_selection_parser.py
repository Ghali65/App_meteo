import pytest
from p_meteo.modules.utils.selection_parser import parse_multi_selection


# -------------------------
# Cas valides
# -------------------------
@pytest.mark.parametrize(
    "selection, max_index, expected",
    [
        ("1", 5, [1]),
        ("3", 5, [3]),
        ("1,3,5", 5, [1, 3, 5]),
        ("1-3", 5, [1, 2, 3]),
        ("2-4,1", 5, [1, 2, 3, 4]),
        ("1,3-5", 5, [1, 3, 4, 5]),
        ("3-3", 5, [3]),  # plage identique
        ("5,4,3,2,1", 5, [1, 2, 3, 4, 5]),  # tri + doublons
        (" 1 , 3 - 4 , 2 ", 5, [1, 2, 3, 4]),  # espaces
    ]
)
def test_parse_multi_selection_valid(selection, max_index, expected):
    assert parse_multi_selection(selection, max_index) == expected


# -------------------------
# Cas invalides
# -------------------------
@pytest.mark.parametrize(
    "selection, max_index",
    [
        ("0", 12),          # trop petit
        ("14", 12),          # trop grand
        ("1,14", 12),        # un seul hors borne invalide tout
        ("a", 12),          # non numérique
        ("1,a", 12),        # mix invalide
        ("1--3", 12),       # mauvais format
        ("3-1", 12),        # plage inversée
        ("3-14", 12),       # plage hors borne
        ("-1", 12),         # négatif
        ("", 12),           # vide
        (None, 12),         # None
    ]
)
def test_parse_multi_selection_invalid(selection, max_index):
    assert parse_multi_selection(selection, max_index) is None
