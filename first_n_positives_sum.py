
def first_n_positive(lst: list[int], n: int) -> list[int]:
    """Returneaza o lista cu elementele pozitive ale altei

    Args:
        lst (list[int]): Lista din care sunt extrase numerele pozitive
        n (int): Numarul de numere pozitive inserate in lista noua

    Returns:
        list[int]: Noua lista cu n elemente pozitive. Daca n este mai mica decat numarul de elemente pozitive din lista initiala, se returneaza None in loc
    """
    positives_list = []

    if n == 0:
        return []

    positives = 0
    for x in lst:
        if x>=0:
            positives_list.append(x)
            positives+=1
        if positives == n:
            return positives_list

    return None

def test_first_n_positive():
    assert first_n_positive([-1,2,4,-5,29,41,-83], 3) == [2,4,29]
    assert first_n_positive([], 0) == []
    assert first_n_positive([-4,-3,2,-5], 2) == None
    assert first_n_positive([41,28,93,52], 4) == [41,28,93,52]

test_first_n_positive()

def first_n_positive_sum(lst: list[int], n: int) -> int:
    """Returneaza suma primelor n numere pozitive dintr-o lista

    Args:
        n (int): Numarul de numere pozitive insumate
        lst (list[int]): Lista din care sunt extrase numerele pozitive

    Returns:
        int: Suma numerelor. Daca sunt mai putin de n numere pozitive in lista se returneaza string-ul "Dimensiunea listei este prea mică" in loc
    """
    positive_list = first_n_positive(lst, n)

    if positive_list == None:
        return "Dimensiunea listei este prea mică"
    else:
        return sum(first_n_positive(lst, n))

def test_first_n_positive_sum():
    assert first_n_positive_sum([10, -3, 25, -1, 3, 25, 18], 3) == 38
    assert first_n_positive_sum([21,48,93,51], 0) == 0
    assert first_n_positive_sum([-4,-3,21] , 2) == "Dimensiunea listei este prea mică"

test_first_n_positive_sum()

