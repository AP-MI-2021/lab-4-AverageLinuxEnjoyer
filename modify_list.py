from math import sqrt

def is_prime(n: int) -> bool:
    """Verifica daca un numar e prim

    Args:
        n (int): Numarul verificat

    Returns:
        bool: True daca e prim, False in caz contrar
    """
    if n < 2:
        return False

    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True

def test_is_prime():
    assert is_prime(17) == True
    assert is_prime(0) == False
    assert is_prime(97) == True
    assert is_prime(45) == False

test_is_prime()


def modify_list(lst: list[float]) -> list:
    """Returneaza lista obținute din lista inițială în care float-urile cu partea întreagă a radicalului număr prim sunt puse ca string-uri cu caracterele în ordine inversă

    Args:
        lst (list[float]): Lista initiala

    Returns:
        list: Lista obtinuta
    """

    sqrts = [int(sqrt(x)) for x in lst]

    for i in range(len(lst)):
        if is_prime(sqrts[i]):
            lst[i] = str(lst[i])[::-1]
    
    return lst

def test_modify_list():
    assert modify_list([10.0, 100.0, 12.45, 50.0, 101.2]) == ['0.01', 100.0, '54.21', '0.05', 101.2]
    assert modify_list([21.0,38.9,66.5,3123.5,123.0,0.65,91.23]) == [21.0,38.9,66.5,3123.5,'0.321',0.65,91.23]
    assert modify_list([16.2, 36.8]) == [16.2, 36.8]
    assert modify_list([]) == []
    

test_modify_list()
