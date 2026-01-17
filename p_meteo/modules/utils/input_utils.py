def ask_yes_no(prompt: str) -> bool:
    """
    Pose une question fermée (O/N) et boucle tant que la réponse n'est pas valide.

    Retourne:
        True  si l'utilisateur répond 'O'
        False si l'utilisateur répond 'N'
    """
    while True:
        choix = input(prompt).strip().upper()
        if choix in ("O", "N"):
            return choix == "O"
        print("❌ Réponse invalide. Tapez O ou N.")


def safe_input_choice(
    prompt: str,
    valid_choices: list[str],
    cast_to_int: bool = False
):
    """
    Demande une saisie utilisateur et vérifie qu'elle fait partie des choix valides.
    Boucle jusqu'à obtenir une valeur correcte.

    Particularités :
    - La saisie est automatiquement convertie en majuscules.
    - Si cast_to_int=True, la valeur retournée est un int, sinon un str.

    Args:
        prompt: Message affiché à l'utilisateur.
        valid_choices: Liste des valeurs acceptées (en str).
        cast_to_int: Si True, convertit la saisie en int avant de la retourner.

    Returns:
        str ou int selon cast_to_int.
    """
    while True:
        choix = input(prompt).strip().upper()

        if choix in valid_choices:
            return int(choix) if cast_to_int else choix

        print(
            f"\n❌ Saisie invalide : '{choix}'. "
            f"Choix possibles : {', '.join(valid_choices)}.\n"
        )


def safe_input_back_or_choice(
    prompt: str,
    valid_choices: list[str],
    back_value: str = "0",
    cast_to_int: bool = False
):
    """
    Variante de safe_input_choice permettant d'inclure un choix 'retour'.

    Comportement :
    - Si l'utilisateur saisit back_value (par défaut "0"), la fonction retourne None.
    - Sinon, elle se comporte comme safe_input_choice.

    Args:
        prompt: Message affiché à l'utilisateur.
        valid_choices: Liste des valeurs acceptées (hors back_value).
        back_value: Valeur spéciale pour signifier un retour / annulation.
        cast_to_int: Si True, convertit la saisie en int avant de la retourner.

    Returns:
        None si back_value est saisi, sinon str ou int selon cast_to_int.
    """
    valid = [back_value] + valid_choices

    choix = safe_input_choice(prompt, valid, cast_to_int=False)

    if choix == back_value:
        return None

    return int(choix) if cast_to_int else choix