import math
działanie = input("Jakie działanie chcesz wykonać? (+ - * / ** lub pierwiastek sumy/różnicy obu cyfr (sqrt+ lub sqrt-)): ")
liczba1 = float(input("Wybierz pierwszą liczbę: "))
liczba2 = float(input("Wybierz drugą liczbę: "))

if działanie == "+":
    wynik = (liczba1 + liczba2)
    print(wynik)
elif działanie == "-":
    wynik = (liczba1 - liczba2)
    print(wynik)
elif działanie == "*":
    wynik = (liczba1 * liczba2)
    print(wynik)
elif działanie == "/":
    wynik = (liczba1 / liczba2)
    print(wynik)
elif działanie == "**":
    wynik = (liczba1 ** liczba2)
    print(wynik)
elif działanie == "sqrt+":
    wynik = math.sqrt(liczba1 + liczba2)
    print(wynik)
elif działanie == "sqrt-":
    wynik = math.sqrt(liczba1 - liczba2)
    print(wynik)
else:
    print("Wprowadzone dane do obliczeń są nieprawdiłowe.")