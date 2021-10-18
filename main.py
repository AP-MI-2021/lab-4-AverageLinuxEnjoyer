from menu import *
from remove_duplicates import remove_duplicates
from positives import first_n_positive_sum


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
            pass

if __name__ == "__main__":
    main()
