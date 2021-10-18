from collections import Counter
from divisors import divisors

def nonduplicates_replaced_with_divisors(lst: list[int]) -> list[int]:
    """Returneaza lista obținuta din lista inițială în care numerele care apar doar o singură dată sunt
înlocuite cu numărul de divizori proprii ai numărului.

    Args:
        lst (list[int]): Lista initiala

    Returns:
        list[int]: Lista obtinuta
    """
    counter = Counter(lst)

    for i in range(len(lst)):
        if counter[lst[i]] == 1:
            lst[i] = divisors(lst[i])

    return lst

def test_nonduplicates_replaced_with_divisors():
    assert nonduplicates_replaced_with_divisors([12,49,49,12,12,53,81,94,5]) == [12, 49, 49, 12, 12, 0, 3, 2, 0]
    assert nonduplicates_replaced_with_divisors([25,13,26,13,19]) == [1,13,2,13,0]
    assert nonduplicates_replaced_with_divisors([]) == []

test_nonduplicates_replaced_with_divisors()