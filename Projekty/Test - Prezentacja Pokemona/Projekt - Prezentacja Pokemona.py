import sys
import requests
import time

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPixmap


class MainWindow(QMainWindow):     # tworzenie klasy, pobiera dziedziczenie z QMainWindow z PySide6
                                    # def - konstruktor, automatyczna funkcja przy tworzeniu okna, pobiera obraz
    def __init__(self, image_path):
        super().__init__()  # zanim przejdzie dalej inicjuje główne dziedziczenie - QMainWindow (białe okno)

        self.setWindowTitle("Pokemon")  # tytuł exe
        self.setGeometry(700, 300, 500, 500)  # X Y szerokość wysokość

        self.label = QLabel(self)  # tworzenie label'u - etykiety
        self.label.setGeometry(0, 0, 500, 500)  # zajmuje całe okno od 0-500, 0-500 # X Y szerokość wysokość

        pixmap = QPixmap(image_path) # władowanie zdjęcia image_path (.png)

        self.label.setPixmap(pixmap)  # label otrzymuje zdjęcie do okazu
        self.label.setScaledContents(True)  # rozciągniecie na całe okno

api_url = "https://pokeapi.co/api/v2"

pokemon_input = input("Choose your pokemon: ").lower()

pokemon_url = f"{api_url}/pokemon/{pokemon_input}"

response = requests.get(pokemon_url)

if response.status_code == 200:

    print("Your pokemon is ready!\n")
    time.sleep(0.3)

    pokemon_stats = response.json()

    print("Stats:")
    print(f'Name: {pokemon_stats["name"].capitalize()}')
    time.sleep(0.2)

    print(f'Weight: {pokemon_stats["weight"] / 10} kg')
    time.sleep(0.2)

    print(f'Height: {pokemon_stats["height"] * 10} cm')
    time.sleep(0.2)

    for stat in pokemon_stats["stats"]:
        stat_name = stat["stat"]["name"].upper()
        base_stat = stat["base_stat"]

        print(f"{stat_name}: {base_stat}")
        time.sleep(0.2)

    image_url = pokemon_stats["sprites"]["front_default"]

    if image_url is None:
        print("This pokemon has no image.")
        sys.exit()

    image = requests.get(image_url)

    if image.status_code == 200:

        with open("pokemon.png", "wb") as file:
            file.write(image.content)

        print("\nYour pokemon will appear soon...")
        time.sleep(0.5)

        app = QApplication(sys.argv)

        window = MainWindow("pokemon.png")
        window.show()

        sys.exit(app.exec())

    else:
        print("Couldn't download image.")

else:
    print("This pokemon doesn't exist.")

