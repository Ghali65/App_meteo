def safe_input_choice(prompt: str, valid_choices: list[str]) -> str:
    """
    Demande une saisie utilisateur et vérifie qu'elle fait partie des choix valides.
    Boucle jusqu'à obtenir une valeur correcte.

    Cette version ne fait pas de cast en int et ne force pas la majuscule :
    elle retourne exactement la chaîne saisie si elle est valide.

    Args:
        prompt: Message affiché à l'utilisateur.
        valid_choices: Liste des valeurs acceptées.

    Returns:
        La saisie utilisateur (str) si elle est valide.
    """
    while True:
        choix = input(prompt).strip()
        if choix in valid_choices:
            return choix
        print(
            f"\n❌ Saisie invalide : '{choix}'. "
            f"Choix possibles : {', '.join(valid_choices)}.\n"
        )