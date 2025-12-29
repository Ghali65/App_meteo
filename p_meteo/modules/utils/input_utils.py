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

def ask_int_in_range(prompt: str, min_val: int, max_val: int) -> int:
    """
    Demande un entier dans une plage donnée.
    Boucle tant que la saisie n'est pas valide.
    """
    while True:
        choix = input(prompt).strip()
        if choix.isdigit():
            choix = int(choix)
            if min_val <= choix <= max_val:
                return choix
        print(f"❌ Entrez un nombre entre {min_val} et {max_val}.")
