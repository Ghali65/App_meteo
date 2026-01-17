from typing import List, Optional


def parse_multi_selection(selection: str, max_index: int) -> Optional[List[int]]:
    """
    Parse une chaîne du type "1,3-5,7" et retourne une liste d'indices valides.

    Règles :
    - Les valeurs simples (ex: "4") sont interprétées comme un indice unique.
    - Les plages (ex: "3-6") sont développées en [3, 4, 5, 6].
    - Les indices doivent être compris entre 1 et max_index.
    - Les doublons sont supprimés.
    - La liste retournée est triée.

    Retourne:
        - Une liste d'entiers si la saisie est valide.
        - None si la saisie est invalide (format ou valeurs hors bornes).
    """
    try:
        result: list[int] = []
        parts = selection.split(",")

        for part in parts:
            part = part.strip()

            # Plage : 3-6
            if "-" in part:
                start, end = map(int, part.split("-"))
                if start < 1 or end > max_index or start > end:
                    raise ValueError
                result.extend(range(start, end + 1))

            # Valeur simple : 4
            else:
                num = int(part)
                if num < 1 or num > max_index:
                    raise ValueError
                result.append(num)

        return sorted(set(result))

    except Exception:
        return None