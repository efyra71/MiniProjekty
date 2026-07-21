import random
import time

while True:
    print()

    while True:
        try:
            ilość_liter = int(input("Ile liter ma posiadać twoje nowe hasło?: "))
            print()
            if ilość_liter < 5:
                print("Twoje nowe hasło musi posiadać co najmniej pięć liter.")
            elif ilość_liter > 20:
                print("Twoje nowe hasło może mieć maksymalnie dwadzieścia liter.")
            else:
                break
        except ValueError:
            print("Podczas zmiany hasła napotkano błąd. Spróbuj ponownie wkrótce.")
            continue

    while True:
        try:
            ilość_cyfr = int(input("Ile cyfr ma posiadać twoje hasło?: "))
            if ilość_cyfr < 1:
                print()
                time.sleep(0.5)
                print("Twoje nowe hasło musi posiadać co najmniej jedną cyfrę.")
                continue
            elif ilość_cyfr > 10:
                print()
                time.sleep(0.5)
                print("Twoje nowe hasło może mieć maksymalnie dziesięć cyfr.")
            else:
                break
        except ValueError:
            print()
            time.sleep(0.5)
            print("Podczas zmiany hasła napotkano błąd. Spróbuj ponownie wkrótce.")
            continue

    print()
    print("Twoje podane dane to: ")
    print()
    time.sleep(0.5)
    print(f"Ilość polskich liter w twoim nowym haśle to: {ilość_liter}.")
    time.sleep(0.5)
    print(f"Ilość cyfr w twoim nowym haśle to: {ilość_cyfr}.")
    print()
    time.sleep(0.5)


    weryfikacja = (input("Czy wprowadzone dane są prawdiłowe? (Tak/Nie): ")).lower()

    if weryfikacja == "tak":
        print()
        time.sleep(0.5)
        print("Poprawnie wprowadziłeś dane do nowego hasła.")
        break
    else:
        print()
        time.sleep(0.5)
        print("W takim razie zaczynamy od początku...")
        time.sleep(1)

alfabet = "abcdefghijklmnopqrstuvwxyz"
cyfry = "1234567890"

hasło = ""

for L in range(ilość_liter):
    litera = random.choice(alfabet)
    hasło = hasło + litera

for C in range(ilość_cyfr):
    cyfra = random.choice(cyfry)
    hasło = hasło + cyfra

lista_znaków = list(hasło)
random.shuffle(lista_znaków)
hasło = "".join(lista_znaków)

print()
print("Generujemy twoje nowe hasło. Potrwa to tylko kilka sekund.")

czas_tworzenia_hasła = random.randint(2,4)
time.sleep(czas_tworzenia_hasła)

print()
print(f"Twoje nowe hasło to: {hasło}.")

time.sleep(0.5)
print("Dziękujemy za korzystanie z naszej strony!")