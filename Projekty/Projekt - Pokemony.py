import requests
import time
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)
        pixmap = QPixmap("pokemon_png")
        label.setPixmap(pixmap)
        label.setScaledContents(True)

api_url = "https://pokeapi.co/api/v2"

pokemon_input = input("Choose your pokemon: ").lower()
pokemon_url = f'{api_url}/pokemon/{pokemon_input}'
response = requests.get(pokemon_url)
if response:
    print("Your pokemon is ready!\n")
    time.sleep(0.3)
    pokemon_stats = response.json()
    print('Stats:')
    print(f'Name: {pokemon_stats["name"].capitalize()}')
    time.sleep(0.2)
    print(f'Weight: {pokemon_stats["weight"]/10}kg')
    time.sleep(0.2)
    print(f'Height: {pokemon_stats["height"]*10}cm')
    time.sleep(0.2)
    for stat in pokemon_stats["stats"]:
        stat_name = stat["stat"]["name"].upper()
        base_stat = stat["base_stat"]
        print(f'{stat_name}: {base_stat}')
        time.sleep(0.2)
    time.sleep(0.2)
    print('\nYour pokemon will appear soon...\n')
    time.sleep(0.4)
    pokemon_png = pokemon_stats['sprites']['front_default']

else:
        print("This pokemon doesn't exist.")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

