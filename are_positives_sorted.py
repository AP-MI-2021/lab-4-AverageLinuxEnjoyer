def are_positives_sorted(lst: list[int]) -> bool:
    """Verifica daca elementele pozitive ale unei liste sunt in ordine crescatoare

    Args:
        lst (list[int]): Lista verificata

    Returns:
        bool: True daca elementele sunt in ordine crescatoare, False in caz contrar
    """
    positive_lst = [x for x in lst if x >= 0]

    if sorted(positive_lst) == positive_lst:
        return True
    else:
        return False

def test_are_positives_sorted():
    assert are_positives_sorted([1,-24,-5,29,14]) == False
    assert are_positives_sorted([41,92,-3,-59, 100]) == True
    assert are_positives_sorted([]) == True

test_are_positives_sorted()

