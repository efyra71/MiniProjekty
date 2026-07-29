import time

def pokaż_ilość_środków():
    print(f"Twoja aktualna ilość środków na koncie to: {środki:.2f}.")

def wpłata():
    ilość_wpłaty = float(input("Ile pieniędzy chcesz wpłacić?: "))
    if ilość_wpłaty < 10:
        print("Minimalna kwota wpłaty wynosi 10zł.")
        return 0
    else:
        return ilość_wpłaty

def wypłata():
    ilość_wypłaty = float(input("Ile pieniędzy chcesz wypłacić?: "))
    if ilość_wypłaty > środki:
        print("Brak wystarczającej ilości środków do wypłaty na koncie.")
        return 0
    elif ilość_wypłaty < 10:
        print("Minimalna kwota wypłaty wynosi 10zł.")
        return 0
    else:
        return ilość_wypłaty

bankomat_działa = True
środki = 0.0

while bankomat_działa == True:

    print("----- BANKOMAT -----")
    print("1. Pokaż ilość środków na koncie")
    print("2. Wpłata")
    print("3. Wypłata")
    print("4. Wyjście")

    wybór = input("Którą operację chcesz wykonać? (1-4): ")

    match wybór:
        case "1":
            time.sleep(0.5)
            pokaż_ilość_środków()
            print()
        case "2":
            time.sleep(0.5)
            kwota = wpłata()
            środki += kwota
            print("Twoja wpłata została zaksięgowana.")
            print()
        case "3":
            time.sleep(0.5)
            kwota = wypłata()
            środki -= kwota
            print("Twoja wypłata została zaksięgowana.")
            print()
        case "4":
            time.sleep(0.5)
            print("Dziękujemy za skorzystanie z naszego bankomatu.")
            print()
            bankomat_działa = False
        case _:
            time.sleep(0.5)
            print("Brak takiej opcji do wyboru.")
            print()

    time.sleep(0.5)