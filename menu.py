
def readList() -> list[float]:
    print("Introdu elementele listei separate printr-o virgula (ex: 5.6,2.9,3.8,-4.2 )")
    lst = input("lista: ")
    lst = [float(x) for x in lst.split(",")]
    
    return lst

def printMenu():
    print("""
    Ce doresti sa faci?
    1) Citirea unei liste de float-uri.
    2) Afisarea tuturor numerelor intregi din lista.
    3) Afisarea celui mai mare numar divizibil cu un numar citit de la tastatura.
    4) Afisarea tuturor numerelor ale caror parte fractionara este palindrom.
    5) Afisarea listei obtinute din lista initiala in care float-urile cu partea intreaga a radicalului numar prim sunt puse ca string-uri cu caracterele in ordine inversa.
    6) Inchidere meniu.
    """)

