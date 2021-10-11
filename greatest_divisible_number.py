
def greatest_divisible_number(lst: list[float], k: int) -> float:
    """Returneaza cel mai mare numar dintr-o lista divizibil cu un intreg k

    Args:
        lst (list[float]): Lista
        k (int): Numarul cu care e verificata divizibilitatea

    Returns:
        float: Cel mai mare numar divizibil cu k
    """
    greatest = float('-inf')
    for x in lst:
        if x % k == 0 and x > greatest:
            greatest = x

    return greatest if greatest != float('-inf') else None


def test_greatest_divisible_number():
    assert greatest_divisible_number([24.5, 56.0, 49.2, 23.0, -3.4], 7) == 56.0
    assert greatest_divisible_number([2.0], 15) == None
    assert greatest_divisible_number([-90.0, 48.0, 53.3, 21.0, 64.2, 89.4], 5) == -90.0
    assert greatest_divisible_number([24.0, 64.0, 53.0, 98.0, 405.0], 2) == 98.0


test_greatest_divisible_number()
