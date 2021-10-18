
def remove_duplicates(lst: list[int]) -> list[int]:
    """Returneaza lista fara elemente duplicate

    Args:
        lst (list[int]): Lista initiala

    Returns:
        list[int]: Lista fara elemente duplicate
    """
    return list(set(lst))