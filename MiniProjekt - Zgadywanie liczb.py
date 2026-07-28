import random
print("------------------------------")
print("--------- ZGADYWANIE ---------")
print("------------------------------")
liczba_docelowa = random.randint(1, 100)
liczba_prób = 0
gracz_szuka_liczby = True

while gracz_szuka_liczby:
    liczba = int(input("Zgadnij liczbę od 1 do 100: "))
    print()
    if liczba < liczba_docelowa:
        print("Szukana liczba jest większa. Spróbuj ponownie.")
        liczba_prób += 1
        continue
    elif liczba > liczba_docelowa:
        print("Szukana liczba jest mniejsza. Spróbuj ponownie.")
        liczba_prób += 1
        continue
    elif liczba == liczba_docelowa:
        print(f"Gratulacje! Udało ci się odgadnąć liczbę. Łączna ilość prób: {liczba_prób}.")
        gracz_szuka_liczby = False
    else:
        print("Wprowadź konkretną cyfrę/liczbę.")

