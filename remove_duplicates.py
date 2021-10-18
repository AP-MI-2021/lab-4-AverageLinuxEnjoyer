
def remove_duplicates(lst: list[int]) -> list[int]:
    """Returneaza lista fara elemente duplicate

    Args:
        lst (list[int]): Lista initiala

    Returns:
        list[int]: Lista fara elemente duplicate
    """
    return list(set(lst))


def test_remove_duplicates():
    assert remove_duplicates([4, 5, 5, 6, 7]) == [4, 5, 6, 7]
    assert remove_duplicates([]) == []
    assert remove_duplicates([-1, 2, 3, 5, 20, -1]) == [2, 3, 5, 20, -1]


test_remove_duplicates()
