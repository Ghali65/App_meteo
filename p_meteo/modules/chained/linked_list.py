class Link:
    """
    Classe représentant un maillon de la liste chaînée.
    Chaque maillon contient une valeur (ex. un viewer) et une référence vers le suivant.
    """

    def __init__(self, value, suivant=None):
        """
        Initialise un maillon.

        Args:
            value: Objet stocké dans le maillon (ex. un viewer S...).
            suivant (Link, optionnel): Maillon suivant dans la liste.
        """
        self.value = value
        self.suivant = suivant

    def get_value(self):
        """Retourne la valeur contenue dans le maillon."""
        return self.value

    def get_suivant(self):
        """Retourne le maillon suivant."""
        return self.suivant

    def set_suivant(self, suivant):
        """Définit le maillon suivant."""
        self.suivant = suivant


class LinkedList:
    """
    Classe représentant une liste chaînée simple.
    Permet d'ajouter des maillons et de parcourir la liste.
    """

    def __init__(self, premier_maillon: Link):
        """
        Initialise la liste avec un premier maillon.

        Args:
            premier_maillon (Link): Premier élément de la liste.
        """
        self.premier_maillon = premier_maillon

    def ajouter_maillon(self, maillon: Link):
        """Ajoute un maillon à la fin de la liste."""
        self.get_dernier().set_suivant(maillon)

    def get_dernier(self):
        """Retourne le dernier maillon de la liste."""
        maillon_actuel = self.premier_maillon
        while maillon_actuel.get_suivant() is not None:
            maillon_actuel = maillon_actuel.get_suivant()
        return maillon_actuel

    def afficher_liste(self):
        """
        Parcourt la liste et appelle la méthode display()
        de chaque objet stocké dans les maillons.
        """
        maillon_actuel = self.premier_maillon
        while maillon_actuel is not None:
            maillon_actuel.get_value().display()
            maillon_actuel = maillon_actuel.get_suivant()
