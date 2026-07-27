def białko():
    białko_posiłek = float(input("Ile gramów białka ma twój posiłek? (g): "))
    if białko_posiłek < 0:
        print("Proszę wpisać nieujemną wartość.")
        return 0
    else:
        return białko_posiłek

def tłuszcz():
    tłuszcz_posiłek = float(input("Ile gramów tłuszczu ma twój posiłek? (g): "))
    if tłuszcz_posiłek  < 0:
        print("Proszę wpisać nieujemną wartość.")
        return 0
    else:
        return tłuszcz_posiłek

def węglowodany():
    węglowodany_posiłek = float(input("Ile gramów węglowodanów ma twój posiłek? (g): "))
    if węglowodany_posiłek  < 0:
        print("Proszę wpisać nieujemną wartość.")
        return 0
    else:
        return węglowodany_posiłek

def kalorie():
    liczba_kalorii = nowe_białko * 4 + nowe_tłuszcz * 9 + nowe_węglowodany * 4
    return liczba_kalorii

kcal_dzień = 2500.0

lista_nazw_posiłków = []
lista_kaloryczna_posiłków = []

if kcal_dzień > 0:
    aplikacja = True
else:
    aplikacja = False

while aplikacja == True:
    print("------- KALKULATOR KALORII -------")
    print("1/P. Dodaj posiłek")
    print("2/K. Sprawdź pozostałą ilość kalorii (dzień)")
    print("3/H. Sprawdź historię dzisiejszych posiłków")
    print("4/Q. Opuść aplikację")
    print("--------------------------------")
    wybór1 = input("Wybierz opcję (1-4): ").upper()
    match wybór1:
        case "2" | "K":
            print(f"Twoja pozostała ilość kalorii w tym dniu wynosi: {kcal_dzień:.2f} kcal.")
        case "4" | "Q":
            print("Dziękujemy, za korzystanie z naszej aplikacji. Pamiętaj, żeby dodać swój następny posiłek!")
            break
        case "3" | "H":
            print("Twoje dzisiejsze posiłki:")
            for nazwa_posiłek, kcal_posiłek in zip(lista_nazw_posiłków, lista_kaloryczna_posiłków):
                print(f"{nazwa_posiłek} - {kcal_posiłek} kcal")


        case "1" | "P":
            print("------ MAKROSKŁADNIKI POSIŁKU ------")
            print("0/N. Wprowadź nazwę posiłku: ")
            print("1/B. Dodaj ilość białka (g)")
            print("2/T. Dodaj ilość tłuszczu (g)")
            print("3/W. Dodaj ilość węglowodanów (g)")
            print("4/P. Dodałem już wszystkie makroskładniki - policz cały posiłek.")
            print("5/Q. Opuść aplikację.")
            print("----------------------------------")

            while True:
                wybór2 = input("Wybierz opcję (0-5): ").upper()
                match wybór2:
                    case "0" | "N":
                        nazwa_posiłku = input("Wprowadź nazwę tego posiłku: ")
                        lista_nazw_posiłków.append(nazwa_posiłku)
                    case "1" | "B":
                        nowe_białko = białko()
                    case "2" | "T":
                        nowe_tłuszcz = tłuszcz()
                    case "3" | "W":
                        nowe_węglowodany = węglowodany()
                    case "4" | "P":
                        print("----------------------------------")
                        print("Dodałeś swój posiłek.")
                        print("Makroskładniki i liczba kalorii twojego posiłku:")
                        print(f"Białko: {nowe_białko:.2f}g")
                        print(f"Tłuszcz: {nowe_tłuszcz:.2f}g")
                        print(f"Węglowodany: {nowe_węglowodany:.2f}g")
                        kalorie()
                        suma_kalorii = kalorie()
                        print(f"Kalorie całego posiłku: {suma_kalorii:.2f} kcal")
                        print("----------------------------------")
                        kcal_dzień -= suma_kalorii
                        print(f"Twoja pozostała ilość kalorii w tym dniu wynosi: {kcal_dzień:.2f} kcal.")
                        print("----------------------------------")
                        lista_kaloryczna_posiłków.append(suma_kalorii)
                        break
                    case "5" | "Q":
                        print("Dziękujemy, za korzystanie z naszej aplikacji. Pamiętaj, żeby dodać swój następny posiłek!")
                        break
                    case _:
                        print("Nie wybrałeś konkretnej opcji. Spróbuj jeszcze raz.")
                        break
        case _:
            print("Nie wybrałeś konkretnej opcji. Spróbuj jeszcze raz.")

    if kcal_dzień > 0:
        continue
    else:
        print("----------------------------------")
        print("Wykorzystałeś limit 2500 kalorii w dzisiejszym dniu.")
        print("Wróć do nas jutro!")
        print("----------------------------------")
        break


