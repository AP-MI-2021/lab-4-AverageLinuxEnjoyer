
def readList():
    print("Scrieti elementele listei separate printr-o virgula:")
    lst = input("Lista:")

    return [int(x) for x in lst.split(",")]


def printMenu():
    print("""
    Ce doresti sa faci?
    1. Citirea unei liste de numere intregi.
    2. Afisarea listei dupa eliminarea duplicatelor
    3. Afișarea sumei primelor n numere pozitive din listă, unde n se citește de la tastatură. Dacă
sunt mai puțin de n numere pozitive în listă, se afișează mesajul “Dimensiunea listei este prea
mică”.
    4. Să se afișeze “DA” în cazul în care toate numerele pozitive din listă sunt în ordine crescătoare și
“NU” altfel.
    5. Afișarea listei obținute din lista inițială în care numerele care apar doar o singură dată sunt
înlocuite cu numărul de divizori proprii ai numărului.
    6. Iesire
    """)

