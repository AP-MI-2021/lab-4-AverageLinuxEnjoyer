import math

def divisors(n: int) -> int:
    """Returneaza numarul de divizori ale unui numar

    Args:
        n (int): Numarul verificat

    Returns:
        int: Numarul de divizori ai numarului verificat
    """
    divs = [1]
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            divs.extend([i, n/i])
    divs.extend([n])
    return len(set(divs)) - 2

def test_divisors():
    assert divisors(26) == 2
    assert divisors(17) == 0
    assert divisors(25) == 1

test_divisors()