from menu import *
from remove_duplicates import remove_duplicates
from first_n_positives_sum import first_n_positive_sum
from are_positives_sorted import are_positives_sorted
from nonduplicates_replaced_with_divisors import nonduplicates_replaced_with_divisors


def main():
    option = ""

    lst = []
    while True:
        printMenu()

        option = input("Optiunea aleasa: ")

        if option == "1":
            lst = readList()
            print(lst)
        elif option == "2":
            no_duplicates = remove_duplicates(lst)
            print(f"Lista {lst} fara duplicate este {no_duplicates}")
        elif option == "3":
            n = int(input("Cat sa fie n?"))
            sum = first_n_positive_sum(lst, n)
            print(f"Suma primelor {n} numere pozitive din lista e {sum}.")
        elif option == "4":
            if are_positives_sorted(lst):
                print("DA")
            else:
                print("NU")
        elif option == "5":
            print(nonduplicates_replaced_with_divisors(lst))
        elif option == "6":
            break
        else:
            print("Aceasta optiune nu exista. Incearca din nou.")

if __name__ == "__main__":
    main()
