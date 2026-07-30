# # name = input("Jak się nazywasz?: ")
# # print(f"Hej {name}, miło mi cię poznać!")
# #
# # while True:
# #     try:
# #         age = int(input("Ile masz lat?: "))
# #         if age == 18:
# #             print("Też mam 18 lat.")
# #         elif age < 18:
# #             print("Jestem od ciebie starszy, mam 18 lat.")
# #         else:
# #             print("Jestem od ciebie młodszy, mam 18 lat.")
# #
# #         break
# #
# #     except ValueError:
# #             print("Miałeś wpisać liczbę, nie tekst. Spróbuj jeszcze raz.")
# #
# # studia = input("Czy planujesz iść na studia w Warszawie?: ").lower()
# # if studia == "tak":
# #     print("Super, ja również planuję iść do Warszawy.")
# # elif studia == "nie":
# #     print("Szkoda, nie spotkamy się.")
# # else:
# #     print("Nie zrozumiałem twojej odpowiedzi, czy możesz powtórzyć?")
# #
# # długość = float(input("Podaj długość prostokąta: "))
# # szerokość = float(input("Podaj szerokość prostokąta: "))
# # wymiary = długość*szerokość
# # print(f"Pole tego konkretnego prostkąta wynosi: {wymiary}")
# #
# # a = float(input("Podaj długość pierwszej podstawy prostopadłościanu: "))
# # b = float(input("Podaj długość drugiej podstawy prostopadłościanu: "))
# # c = float(input("Podaj długość wysokości prostopadłościanu: "))
# # V = a*b*c
# # Pc = 2*a*b + 2*b*c + 2*a*c
# #
# # print(f"Objętość tego prostopadłościanu wynosi: {V}")
# # print(f"Pole powierzchni całkowitej tego protopadłościanu wynosi: {Pc}")
#
#
#
# # item = input("Jaki item chciałbyś kupić?: ")
# # cena = float(input("Jaka jest cena tego itemu?:  "))
# # ilość = int(input("Ile chcesz tych itemów zakupić?: "))
# # koszt_całkowity = int(ilość * cena)
# #
# # print(f"Twoje zakupy to: {ilość}x {item}")
# # print(f"Łącznie wydałeś {koszt_całkowity} golda.")
# #
# # import random
# #
# # bok1 = random.randint(1, 20)
# # bok2 = random.randint(1, 20)
# #
# # print(f"Długości boków prostokąta wynoszą {bok1} oraz {bok2}.")
# #
# # while True:
# #     try:
# #         odpowiedź = float(input("Ile wynosi pole tej figury?: "))
# #         if odpowiedź == bok1*bok2:
# #             print("Świetnie! To poprawna odpowiedź.")
# #             break
# #         else:
# #             print("Odpowiedź niepoprawna, spróbuj policzyć jeszcze raz.")
# #     except ValueError:
# #         print("Odpowiedź musi być w postaci liczby całkowitej, spróbuj jeszcze raz.")
# #
# # import math
# # działanie = input("Jakie działanie chcesz wykonać? (+ - * / ** lub pierwiastek sumy/różnicy obu cyfr (sqrt+ lub sqrt-)): ")
# # liczba1 = float(input("Wybierz pierwszą liczbę: "))
# # liczba2 = float(input("Wybierz drugą liczbę: "))
# #
# # if działanie == "+":
# #     wynik = (liczba1 + liczba2)
# #     print(wynik)
# # elif działanie == "-":
# #     wynik = (liczba1 - liczba2)
# #     print(wynik)
# # elif działanie == "*":
# #     wynik = (liczba1 * liczba2)
# #     print(wynik)
# # elif działanie == "/":
# #     wynik = (liczba1 / liczba2)
# #     print(wynik)
# # elif działanie == "**":
# #     wynik = (liczba1 ** liczba2)
# #     print(wynik)
# # elif działanie == "sqrt+":
# #     wynik = math.sqrt(liczba1 + liczba2)
# #     print(wynik)
# # elif działanie == "sqrt-":
# #     wynik = math.sqrt(liczba1 - liczba2)
# #     print(wynik)
# # else:
# #     print("Wprowadzone dane do obliczeń są nieprawdiłowe.")
# #
#
# # import random
# # saldo = 1000
# #
# # while saldo > 0:
# #     print(f"Twoje dostępne środki to: {saldo} PLN")
# #
# #     try:
# #         bet = float(input("Ile pieniędzy chcesz postawić?: "))
# #
# #         if bet > saldo:
# #             print("Nie masz wystarczającej ilości środków do gry.")
# #             continue
# #
# #         elif bet < saldo:
# #             print("Życzymy wygranej!")
# #
# #         elif bet == saldo:
# #             weryfikacja = input("Czy na pewno chcesz przeznaczyć całe swoje pieniądze? (Tak/Nie): ").lower()
# #             if weryfikacja == "tak":
# #                 print("Okej, w takim razie życzymy miłej gry.")
# #             elif weryfikacja == "nie":
# #                 print("Jeżeli nie jesteś pewny, nie stawiaj całych pieniędzy na jedno zdarzenie.")
# #                 continue
# #
# #     except ValueError:
# #         print("Wprowadzone dane są nieprawdiłowe.")
# #         continue
# #
# #     wynik_meczu = random.randint(1, 100)
# #
# #     kurs = 2.0
# #     podatek = 0.12
# #
# #     if wynik_meczu > 50:
# #         saldo = saldo - bet + bet*kurs*(1-podatek)
# #         print(f"Gratulację wygrałeś. Twoje nowe saldo to {saldo:.2f} PLN.")
# #     else:
# #         saldo = saldo - bet
# #         print(f"Niestety, przegrałeś. Twoje nowe saldo to {saldo:.2f} PLN.")
#
# # numer = 10
# #
# # max_numer = "wyższy" if numer > 9 else "niższy"
# # print(max_numer)
#
#
# # hasło = input("Wpisz swoje nowe hasło: ")
# #
# # if len(hasło) > 12:
# #     print("Hasło może posiadać maksymalnie 12 znaków.")
# # elif len(hasło) < 4:
# #     print("Hasło musi posiadać conajmniej 4 znaki.")
# # elif hasło.isalpha():
# #     print("Hasło musi posiadać conajmniej 1 cyfrę.")
# #
# # else:
# #     print(f"Twoje nowe hasło to {hasło}.")
#
#
#
# # import time
# #
# # czas = int(input("Wpisz ilość czasu: "))
# #
# # for x in reversed(range(1, czas + 1)):
# #     print(x)
# #     time.sleep(.5)
# #
# # print("Czas minął.")
#
# # liczba = float(input("Podaj liczbę: "))
# # parzystość = liczba%2
# # if parzystość == 0:
# #     print("Liczba jest parzysta.")
# # else:
# #     print("Liczba jest nieparzysta.")
#
# # import time
# #
# # czas = int(input("Podaj czas w sekundach: "))
# #
# # for sekundy in range(czas, 0, -1):
# #     print(sekundy)
# #     time.sleep(1)
# #
# # print("Czas się skonczył.")
#
# # import random
# # import time
#
# # liczba = random.randint(1,100)
# #
# # while True:
# #     try:
# #         zgadnij = int(input("Zgadnij liczbę od 1 do 100: "))
# #
# #         if zgadnij > liczba:
# #             print("Docelowa liczba jest mniejsza. Spróbuj ponownie.")
# #
# #         elif zgadnij < liczba:
# #             print("Docelowa liczba jest większa. Spróbuj ponownie.")
# #
# #         elif zgadnij == liczba:
# #             print(f"Gratulację! Szukana liczba to: {liczba}.")
# #             break
# #
# #     except ValueError:
# #         print("Wprowadzone dane są nieprawdidłowe. Wprowadź konkretnę liczbę.")
# #         continue
#
# # import random
# # import time
# #
# # while True:
# #     print()
# #
# #     while True:
# #         try:
# #             ilość_liter = int(input("Ile liter ma posiadać twoje nowe hasło?: "))
# #             print()
# #             if ilość_liter < 5:
# #                 print("Twoje nowe hasło musi posiadać co najmniej pięć liter.")
# #             elif ilość_liter > 20:
# #                 print("Twoje nowe hasło może mieć maksymalnie dwadzieścia liter.")
# #             else:
# #                 break
# #         except ValueError:
# #             print("Podczas zmiany hasła napotkano błąd. Spróbuj ponownie wkrótce.")
# #             continue
# #
# #     while True:
# #         try:
# #             ilość_cyfr = int(input("Ile cyfr ma posiadać twoje hasło?: "))
# #             if ilość_cyfr < 1:
# #                 print()
# #                 time.sleep(0.5)
# #                 print("Twoje nowe hasło musi posiadać co najmniej jedną cyfrę.")
# #                 continue
# #             elif ilość_cyfr > 10:
# #                 print()
# #                 time.sleep(0.5)
# #                 print("Twoje nowe hasło może mieć maksymalnie dziesięć cyfr.")
# #             else:
# #                 break
# #         except ValueError:
# #             print()
# #             time.sleep(0.5)
# #             print("Podczas zmiany hasła napotkano błąd. Spróbuj ponownie wkrótce.")
# #             continue
# #
# #     print()
# #     print("Twoje podane dane to: ")
# #     print()
# #     time.sleep(0.5)
# #     print(f"Ilość polskich liter w twoim nowym haśle to: {ilość_liter}.")
# #     time.sleep(0.5)
# #     print(f"Ilość cyfr w twoim nowym haśle to: {ilość_cyfr}.")
# #     print()
# #     time.sleep(0.5)
# #
# #
# #     weryfikacja = (input("Czy wprowadzone dane są prawdiłowe? (Tak/Nie): ")).lower()
# #
# #     if weryfikacja == "tak":
# #         print()
# #         time.sleep(0.5)
# #         print("Poprawnie wprowadziłeś dane do nowego hasła.")
# #         break
# #     else:
# #         print()
# #         time.sleep(0.5)
# #         print("W takim razie zaczynamy od początku...")
# #         time.sleep(1)
# #
# # alfabet = "abcdefghijklmnopqrstuvwxyz"
# # cyfry = "1234567890"
# #
# # hasło = ""
# #
# # for L in range(ilość_liter):
# #     litera = random.choice(alfabet)
# #     hasło = hasło + litera
# #
# # for C in range(ilość_cyfr):
# #     cyfra = random.choice(cyfry)
# #     hasło = hasło + cyfra
# #
# # lista_znaków = list(hasło)
# # random.shuffle(lista_znaków)
# # hasło = "".join(lista_znaków)
# #
# # print()
# # print("Generujemy twoje nowe hasło. Potrwa to tylko kilka sekund.")
# #
# # czas_tworzenia_hasła = random.randint(2,4)
# # time.sleep(czas_tworzenia_hasła)
# #
# # print()
# # print(f"Twoje nowe hasło to: {hasło}.")
# #
# # time.sleep(0.5)
# # print("Dziękujemy za korzystanie z naszej strony!")
#
#
# # championy = ["Ahri", "Akali", "Vladimir", "Irelia"]
# #
# # # for champion in championy:
# # #     print(champion)
# #
# # championy.append("Vex")
# # print(championy)
# # championy.remove("Vladimir")
# # print(championy)
# # championy.insert(2, "Annie")
# # print(championy)
# # championy.sort()
# # print(championy)
#
# # telefon = [(1, 2, 3),
# #            (4, 5, 6),
# #            (7, 8, 9),
# #            ("*", 0, "#")]
# #
# # for set in telefon:
# #     for numer in set:
# #         print(numer, end=" ")
# #     print(" ")
#
# # stolica = {"Polska": "Warszawa"}
# # print(stolica.get("Polska"))
# #
# #
#
# # import random
# # możliwości = ("papier", "kamień", "nożyce")
# # wybór_1 = random.choice(możliwości)
# # wybór_2 = input("Wybierz papier/kamień/nożyce: ").lower()
# #
# # while True:
# #     if wybór_2 == "papier" and wybór_1 == "kamień":
# #         print(f"Wybrałeś {wybór_2}, a twój rywal wybrał {wybór_1}. Wygrywasz!")
# #         break
# #     elif wybór_2 == "kamień" and wybór_1 == "nożyce":
# #         print(f"Wybrałeś {wybór_2}, a twój rywal wybrał {wybór_1}. Wygrywasz!")
# #         break
# #     elif wybór_2 == "nożyce" and wybór_1 == "papier":
# #         print(f"Wybrałeś {wybór_2}, a twój rywal wybrał {wybór_1}. Wygrywasz!")
# #         break
# #     elif wybór_2 == "papier" and wybór_1 == "nożyce":
# #         print(f"Wybrałeś {wybór_2}, a twój rywal wybrał {wybór_1}. Przegrywasz.")
# #         break
# #     elif wybór_2 == "kamień" and wybór_1 == "papier":
# #         print(f"Wybrałeś {wybór_2}, a twój rywal wybrał {wybór_1}. Przegrywasz.")
# #         break
# #     elif wybór_2 == "nożyce" and wybór_1 == "kamień":
# #         print(f"Wybrałeś {wybór_2}, a twój rywal wybrał {wybór_1}. Przegrywasz.")
# #         break
# #     elif wybór_2 == wybór_1:
# #         print(f"Wybrałeś {wybór_2}, a twój rywal też wybrał {wybór_1}. Remis!")
# #         break
# #     else:
# #         print("Niepoprawny wybór! Wpisz dokładnie: papier, kamień lub nożyce.")
# #         wybór_2 = input("Wybierz papier/kamień/nożyce: ").low
#
# # def gry_do_zagrania():
# #     print("Zagraj w Hollow Knight")
# #     print("Zagraj w The Last of Us 2")
# #     print("Zagraj w Minecraft")
# #
# # for polecenie in range(3):
# #     print()
# #     gry_do_zagrania()
# #     print()
# #
# # def dodawanie(a,b,c):
# #     x = a + b + c
# #     return x
# #
# # print(dodawanie(2,3,4))
# #
# # def zestaw(imię, drugie_imię, nazwisko):
# #     imię = imię.capitalize()
# #     drugie_imię = drugie_imię.capitalize()
# #     nazwisko = nazwisko.capitalize()
# #     return imię + ", " + drugie_imię + " " + nazwisko
# #
# # print(zestaw("Jakub", "Franciszek", "Nowak"))
# #
# # import time
# # def odliczanie(koniec, start=0):
# #     for x in reversed(range(start, koniec+1)):
# #         print(x)
# #         time.sleep(1)
# #     print("Czas się skończył.")
# #
# # # odliczanie(długośc odliczania w sekundach)
# # odliczanie(10)
#
#
# # import time
# #
# # prefiks = input("Wpisz swój krajowy prefiks: ")
# # time.sleep(0.3)
# # print()
# # numer = input("Wpisz swój numer telefonu (bez spacji): ")
# #
# # czesc1 = numer[:3]
# # czesc2 = numer[3:6]
# # czesc3 = numer[6:]
# #
# # sformatowany_numer = f"{czesc1}-{czesc2}-{czesc3}"
# #
# # def numer_telefonu(numer):
# #     pełny_numer_telefonu = pelny_numer_telefonu = f"{prefiks} {sformatowany_numer}"
# #     print(f"Twój numer telefonu to {pełny_numer_telefonu}.")
# #
# # numer_telefonu(numer)
# #
# # def dane_zamieszkania(**kwargs):
# #    for key, value in kwargs.items():
# #        print(f"{key}: {value}")
# #
# # dane_zamieszkania(ulica = "Floriańska",
# #                   numer_ulicy = 10,
# #                 kraj = "Polska",
# #                   miasto = "Wałbrzych")
#
# # dzień_tygodnia = input("Jaki jest dzisiaj dzień tygodnia?: ").lower()
# #
# # match dzień_tygodnia:
# #     case "poniedziałek":
# #         print("Dopiero początek tygodnia...")
# #     case "sobota" | "niedziela":
# #         print("Weekend!")
# #     case "piątek":
# #         print("Jutro weekend!")
# #     case _:
# #         print("Zwykły dzień roboczy.")
#
#
#
#
# import time
#
# def pokaż_ilość_środków():
#     print(f"Twoja aktualna ilość środków na koncie to: {środki:.2f}.")
#
# def wpłata():
#     ilość_wpłaty = float(input("Ile pieniędzy chcesz wpłacić?: "))
#     if ilość_wpłaty < 10:
#         print("Minimalna kwota wpłaty wynosi 10zł.")
#         return 0
#     else:
#         return ilość_wpłaty
#
# def wypłata():
#     ilość_wypłaty = float(input("Ile pieniędzy chcesz wypłacić?: "))
#     if ilość_wypłaty > środki:
#         print("Brak wystarczającej ilości środków do wypłaty na koncie.")
#         return 0
#     elif ilość_wypłaty < 10:
#         print("Minimalna kwota wypłaty wynosi 10zł.")
#         return 0
#     else:
#         return ilość_wypłaty
#
# bankomat_działa = True
# środki = 0.0
#
# while bankomat_działa == True:
#
#     print("----- BANKOMAT -----")
#     print("1. Pokaż ilość środków na koncie")
#     print("2. Wpłata")
#     print("3. Wypłata")
#     print("4. Wyjście")
#
#     wybór = input("Którą operację chcesz wykonać? (1-4): ")
#
#     match wybór:
#         case "1":
#             time.sleep(0.5)
#             pokaż_ilość_środków()
#             print()
#         case "2":
#             time.sleep(0.5)
#             kwota = wpłata()
#             środki += kwota
#             print("Twoja wpłata została zaksięgowana.")
#             print()
#         case "3":
#             time.sleep(0.5)
#             kwota = wypłata()
#             środki -= kwota
#             print("Twoja wypłata została zaksięgowana.")
#             print()
#         case "4":
#             time.sleep(0.5)
#             print("Dziękujemy za skorzystanie z naszego bankomatu.")
#             print()
#             bankomat_działa = False
#         case _:
#             time.sleep(0.5)
#             print("Brak takiej opcji do wyboru.")
#             print()
#
#     time.sleep(0.5)
#
#

# import random
# import string
#
# znaki = " " + string.punctuation + string.ascii_letters + string.digits
# znaki = list(znaki)
# kod = znaki.copy()
# random.shuffle(kod)
#
# # print(znaki)
# # print(kod)
#
# tekst_przed = input("Wpisz swoją wiadomość: ")
# tekst_po = ""
#
# for litera in tekst_przed:                #program sprawdza wiadomość jako string i przejeżdza po każdej literce
#     zmiana = znaki.index(litera)
#     tekst_po += kod[zmiana]
#
# print(f"Tekst przed: {tekst_przed}")
# print(f"Tekst_po: {tekst_po}")
# import random
#
# class Champion:
#     def __init__(self, name, gender, position, resource):
#         self.name = name
#         self.gender = gender
#         self.position = position
#         self.resource = resource
#
# champions = []
#
# with open("champions.txt", 'r', encoding="utf-8") as file:
#     for line in file:
#         line = line.strip()
#         if line: # if line exists
#             parts = [part.strip() for part in line.split(',')]
#             if len(parts) == 4:
#                 name, gender, position, resource = parts
#                 champions.append(Champion(name, gender, position, resource))
#
# champion = random.choice(champions)
#
# print(
#     f'\n Your champion stats:'
#     f'\nName: {champion.name}'
#     f'\nGender: {champion.gender}'
#     f'\nPosition: {champion.position}'
#     f'\nResource: {champion.resource}'
# )

# # import os
# import random
#
# # file_path = 'C:/Users/Gaweł/Desktop/test.txt'
# # if os.path.exists(file_path):
# #     print("This file exists.\n")
#
# with open("Kurs/numbers.txt", "w") as file:
#     for i in range(1, 100):
#         number = str(random.randint(1, 10))
#         file.write(f"{number}\n")
#
# number_to_find = str(random.randint(1,10))
# numbers_from_file = []
#
# with open("Kurs/numbers.txt", "r", encoding="utf-8") as file:
#     for line in file:
#
#         numbers_from_file.append(line.strip())
#
#     if number_to_find in numbers_from_file:
#         print(f"\nNumber '{number_to_find}' was found {numbers_from_file.count(number_to_find)} times in the list.")
#     else:
#         print(f"\nThere was no number '{number_to_find}' in the list.")






















