import time
import os
def czysta_strona():
    os.system('cls' if os.name == 'nt' else 'clear')

lista_zadań = []
aplikacja_działa = True

while aplikacja_działa:
    time.sleep(1.5)
    czysta_strona()

    print("------------------------------------")
    print("------------ TO-DO LIST ------------")
    print("------------------------------------")
    print("1./+ Dodaj nowe zadanie")
    print("2./- Zaznacz zadanie jako wykonane")
    print("3. Pokaż moje aktualne zadania")
    print("4. Opuść aplikację")
    print()

    wybór1 = input("Co chcesz zrobić? Wybierz spośród 1-4: ")
    match wybór1:
        case "1" | "+":
            nowe_zadanie = input("Jakie zadanie chcesz dodać?: ").upper()
            lista_zadań.append(nowe_zadanie)
            print("-----------------------------------------------")
            print(f"Poprawnie dodano nowe zadanie - {nowe_zadanie}.")
            print("-----------------------------------------------")
        case "2" | "-":
            if not lista_zadań:
                print("---------------------------------------")
                print("Twoja lista zadań jest aktualnie pusta!")
                print("---------------------------------------")
            if lista_zadań:
                print("Twoja aktualna lista zadań:")
                for zadanie in lista_zadań:
                    print(f" - {zadanie}")
                wybór2 = input("Które zadanie chcesz zaznaczyć jako wykonane?: ").upper()
                if wybór2 not in lista_zadań:
                    print("----------------------------------------")
                    print("Takiego zadania nie ma na twojej liście.")
                    print("----------------------------------------")
                else:
                    print(f"Zadanie: {wybór2} - wykonane!")
                    lista_zadań.remove(wybór2)
        case "3":
            if not lista_zadań:
                print("---------------------------------------")
                print("Twoja lista zadań jest aktualnie pusta!")
                print("---------------------------------------")
            if lista_zadań:
                print("Twoja aktualna lista zadań:")
                for zadanie in lista_zadań:
                    print(f" - {zadanie}")
                while True:
                    powrót = input("\nNaciśnij Enter, aby wrócić do początku: ")
                    if powrót == "":
                        break
                    else:
                        print("Nie wpisuj nic, po prostu wciśnij klawisz Enter.")

        case "4":
            print("Do zobaczenia wkrótce!")
            aplikacja_działa = False
