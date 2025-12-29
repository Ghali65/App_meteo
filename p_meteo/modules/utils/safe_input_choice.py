
def safe_input_choice(prompt: str, valid_choices: list[str]) -> str:
    """
    Demande une saisie utilisateur et vérifie qu'elle fait partie des choix valides.
    Boucle jusqu'à obtenir une valeur correcte.
    """
    while True:
        choix = input(prompt).strip()
        if choix in valid_choices:
            return choix
        print(f"\n❌ Saisie invalide : '{choix}'. Choix possibles : {', '.join(valid_choices)}.\n")
