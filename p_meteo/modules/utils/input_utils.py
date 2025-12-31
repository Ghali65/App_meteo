def ask_yes_no(prompt: str) -> bool:
    """
    Pose une question O/N et boucle tant que la réponse n'est pas valide.
    Retourne True pour O, False pour N.
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

    Si cast_to_int=True, retourne un int au lieu d'un str.
    La saisie est automatiquement convertie en majuscules.
    """
    while True:
        choix = input(prompt).strip().upper()

        if choix in valid_choices:
            return int(choix) if cast_to_int else choix

        print(f"\n❌ Saisie invalide : '{choix}'. Choix possibles : {', '.join(valid_choices)}.\n")


def safe_input_back_or_choice(
    prompt: str,
    valid_choices: list[str],
    back_value: str = "0",
    cast_to_int: bool = False
):
    """
    Variante de safe_input_choice permettant d'inclure un choix 'retour'.
    Retourne None si l'utilisateur choisit back_value.
    """
    valid = [back_value] + valid_choices

    choix = safe_input_choice(prompt, valid, cast_to_int=False)

    if choix == back_value:
        return None

    return int(choix) if cast_to_int else choix