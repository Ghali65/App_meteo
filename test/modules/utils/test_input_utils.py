import builtins
import pytest

from p_meteo.modules.utils.input_utils import (
    ask_yes_no,
    safe_input_choice,
    safe_input_back_or_choice,
)


# ----------------------------------------------------------------------
# 🔧 Utilitaire : mocker input() avec une liste de réponses successives
# ----------------------------------------------------------------------
def mock_inputs(monkeypatch, inputs):
    """Simule plusieurs appels successifs à input()."""
    iterator = iter(inputs)
    monkeypatch.setattr(builtins, "input", lambda _: next(iterator))


# ----------------------------------------------------------------------
# 🔥 TESTS ask_yes_no() — version paramétrée
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "user_input, expected",
    [
        (["o"], True),
        (["O"], True),
        (["n"], False),
        (["N"], False),
    ]
)
def test_ask_yes_no_param(monkeypatch, user_input, expected):
    mock_inputs(monkeypatch, user_input)
    assert ask_yes_no("Q? ") is expected


def test_ask_yes_no_invalid_then_valid(monkeypatch, capsys):
    mock_inputs(monkeypatch, ["x", "O"])
    assert ask_yes_no("Q? ") is True

    captured = capsys.readouterr().out
    assert "❌ Réponse invalide" in captured


# ----------------------------------------------------------------------
# 🔥 TESTS safe_input_choice() — version paramétrée
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "inputs, valid, expected",
    [
        (["A"], ["A", "B"], "A"),
        (["b"], ["A", "B"], "B"),
        (["x", "A"], ["A", "B"], "A"),  # invalide puis valide
    ]
)
def test_safe_input_choice_param(monkeypatch, inputs, valid, expected):
    mock_inputs(monkeypatch, inputs)
    assert safe_input_choice("Q? ", valid) == expected


@pytest.mark.parametrize(
    "inputs, valid, expected",
    [
        (["1"], ["1", "2"], 1),
        (["2"], ["1", "2"], 2),
    ]
)
def test_safe_input_choice_int_param(monkeypatch, inputs, valid, expected):
    mock_inputs(monkeypatch, inputs)
    assert safe_input_choice("Q? ", valid, cast_to_int=True) == expected


def test_safe_input_choice_invalid_then_valid(monkeypatch, capsys):
    mock_inputs(monkeypatch, ["X", "B"])
    assert safe_input_choice("Q? ", ["A", "B"]) == "B"

    captured = capsys.readouterr().out
    assert "❌ Saisie invalide" in captured


# ----------------------------------------------------------------------
# 🔥 TESTS safe_input_back_or_choice() — version paramétrée
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "inputs, valid, back, expected",
    [
        (["0"], ["1", "2"], "0", None),
        (["1"], ["1", "2"], "0", "1"),
        (["2"], ["1", "2"], "0", "2"),
        (["x", "1"], ["1", "2"], "0", "1"),  # invalide puis valide
    ]
)
def test_safe_input_back_or_choice_param(monkeypatch, inputs, valid, back, expected):
    mock_inputs(monkeypatch, inputs)
    assert safe_input_back_or_choice("Q? ", valid, back_value=back) == expected


@pytest.mark.parametrize(
    "inputs, valid, expected",
    [
        (["3"], ["3", "4"], 3),
        (["4"], ["3", "4"], 4),
    ]
)
def test_safe_input_back_or_choice_int_param(monkeypatch, inputs, valid, expected):
    mock_inputs(monkeypatch, inputs)
    assert safe_input_back_or_choice("Q? ", valid, cast_to_int=True) == expected
