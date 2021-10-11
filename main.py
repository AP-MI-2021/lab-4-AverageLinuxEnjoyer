import menu
from greatest_divisible_number import greatest_divisible_number
from modify_list import modify_list

def main():
    option = ''
    floats = []

    while True:
        menu.printMenu()
        option = input("Optiune meniu: ")

        if option == '1':
            floats = menu.readList()
        elif option == '2':
            print(f"Numerele intregi din lista sunt: {[x for x in floats if x == int(x)]}")
        elif option == '3':
            k = int(input("Cu ce numar sa se verifice divizibilitatea?"))
            print(f"Cel mai mare numar divizibil cu {k} din lista data e {greatest_divisible_number(floats, k)}")
        elif option == '4':
            print(f"Float-urile din lista a caror parte fractionara este palindrom sunt: {[x for x in floats if str(x).split('.')[1] == str(x).split('.')[1][::-1]]}")
        elif option == '5':
            print(f"In urma modificarii, lista arata asa: {modify_list(floats)}")
        elif option == '6':
            break


if __name__ == "__main__":
    main()