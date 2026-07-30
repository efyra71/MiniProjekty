# import os
import random

# file_path = 'C:/Users/Gaweł/Desktop/test.txt'
# if os.path.exists(file_path):
#     print("This file exists.\n")

with open("numbers.txt", "w") as file:
    for i in range(1, 100):
        number = str(random.randint(1, 10))
        file.write(f"{number}\n")

number_to_find = str(random.randint(1,10))
numbers_from_file = []

with open("numbers.txt", "r", encoding="utf-8") as file:
    for line in file:

        numbers_from_file.append(line.strip())

    if number_to_find in numbers_from_file:
        print(f"\nNumber '{number_to_find}' was found {numbers_from_file.count(number_to_find)} times in the list.")
    else:
        print(f"\nThere was no number '{number_to_find}' in the list.")