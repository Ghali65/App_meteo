from typing import List, Optional

def parse_multi_selection(selection: str, max_index: int) -> Optional[List[int]]:
    """
    Parse une chaîne du type "1,3-5,7" et retourne une liste d'indices valides.
    Retourne None si la saisie est invalide.
    """
    try:
        result = []
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
