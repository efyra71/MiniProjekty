import random
import time
saldo = 1000
podatek = 0.12

while saldo > 0:
    print(f"Twoje dostępne środki to: {saldo:.2f} PLN")
    print()

    try:
        bet = float(input("Ile pieniędzy chcesz postawić?: "))
        if bet <= 0:
            print("Stawka musi być większa niż 0 PLN!")
            print()
            continue

        elif bet > saldo:
            print("Nie masz wystarczającej ilości środków do gry.")
            print()
            continue

        elif bet < saldo:
            print("Życzymy wygranej!")
            print()

        elif bet == saldo:
            weryfikacja = input("Czy na pewno chcesz przeznaczyć całe swoje pieniądze? (Tak/Nie): ").lower()
            if weryfikacja == "tak":
                time.sleep(1)
                print("Okej, w takim razie życzymy miłej gry.")
                print()
            elif weryfikacja == "nie":
                print("Jeżeli nie jesteś pewny, nie stawiaj całych pieniędzy na jedno zdarzenie.")
                print()
                continue

    except ValueError:
        print("Wprowadzone dane są nieprawdiłowe.")
        print()
        continue

    try:
        kurs = float(input("Na jakim kursie planujesz zagrać?: "))
        if kurs <= 1:
            print("Podany kurs musi być wyższy niż 1.0!")
            print()
            continue
        else:
            print(f"Twój wybrany kurs to {kurs}. Mecz rozpocznie się wkrótce.")
            print()
            time.sleep(1)
    except ValueError:
        print()
        print("Wprowadzone dane są nieprawdiłowe.")
        continue

    print("Mecz się rozpoczął... Trwa analiza kuponu...")
    time.sleep(1.5)
    print()

    print("Trwa druga połowa, emocje sięgają zenitu...")
    time.sleep(1.5)
    print()

    print("Wynik meczu to... ")
    time.sleep(2)
    print()

    wynik_meczu = random.randint(1,100)

    if wynik_meczu <= (100/kurs):
        saldo = saldo - bet + bet * kurs * (1 - podatek)
        print(f"ZIELONE, wygrałeś! Twoje nowe saldo to {saldo:.2f} PLN.")
    else:
        saldo = saldo - bet
        print(f"CZERWONE, przegrałeś. Twoje nowe saldo to {saldo:.2f} PLN.")
    if saldo == 0:
        print()
        print("Informujemy cię, że przegrałeś wszystkie swoje pieniądze.")





