"""
Implémentation d'une liste chaînée simple utilisée pour enchaîner les viewers.
"""

from __future__ import annotations
from typing import Any, Optional


class Link:
    """
    Représente un maillon de la liste chaînée.
    Contient une valeur (ex. un viewer) et une référence vers le maillon suivant.
    """

    def __init__(self, value: Any, suivant: Optional["Link"] = None) -> None:
        self.value = value
        self.suivant = suivant

    def get_value(self) -> Any:
        """Retourne la valeur contenue dans le maillon."""
        return self.value

    def get_suivant(self) -> Optional["Link"]:
        """Retourne le maillon suivant."""
        return self.suivant

    def set_suivant(self, suivant: Optional["Link"]) -> None:
        """Définit le maillon suivant."""
        self.suivant = suivant


class LinkedList:
    """
    Liste chaînée simple permettant d'ajouter des maillons
    et de parcourir les viewers dans l'ordre.
    """

    def __init__(self, premier_maillon: Link) -> None:
        self.premier_maillon = premier_maillon

    def append(self, maillon: Link) -> None:
        """Ajoute un maillon à la fin de la liste."""
        self.get_last().set_suivant(maillon)

    def get_last(self) -> Link:
        """Retourne le dernier maillon de la liste."""
        maillon = self.premier_maillon
        while maillon.get_suivant() is not None:
            maillon = maillon.get_suivant()
        return maillon

    def __iter__(self):
        """Permet d'itérer directement sur les valeurs de la liste."""
        maillon = self.premier_maillon
        while maillon is not None:
            yield maillon.get_value()
            maillon = maillon.get_suivant()

    def display_all(self) -> None:
        """Appelle display() sur chaque viewer de la liste."""
        for viewer in self:
            viewer.display()
