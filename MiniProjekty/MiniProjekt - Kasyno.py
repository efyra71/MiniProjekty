import random
import time
print("--------------------------------")
print("------- GAMBLING - SLOTS -------")
print("--------------------------------")

play_count = 0
win_count = 0
lose_count = 0

def restart():
    while True:
        restart = input("Would you like to play again? (Yes - Enter / No - Q): ").upper()
        if restart == "":
            return True
        elif restart == "Q":
            return False
        else:
            print("Hit 'Enter' to play again or 'Q' to quit the game.")


symbole = [
    ["🍒", "🍋", "🔔", "💎", "👑", "⭐️", "🍀"],
    ["🍒", "🍋", "💎", "👑", "⭐️", "🍀"],
    ["🍒", "💎", "👑", "⭐️", "🍀"],
    ["💎", "👑", "⭐️", "🍀"],
    ["💎", "⭐️", "🍀"]
           ]


while True:
    lista_symbole = random.choice(symbole)
    los1 = random.choice(lista_symbole)
    los2 = random.choice(lista_symbole)
    los3 = random.choice(lista_symbole)
    print(f"\n[ {los1} | {los2} | {los3} ]")

    if los1 == los2 == los3:
        print("BIG WIN!")
        play_count += 1
        win_count += 1
        print(f"\nYour total play count: {play_count} spins.")
    else:
        print("YOU LOSE")
        play_count += 1
        lose_count += 1
        print(f"\nYour total play count: {play_count} spins.")

    if restart() == False:
        print("\nYour stats for today:")
        print(f"✅ Win: {win_count} times")
        print(f"❌ Lose: {lose_count} times")
        win_ratio = ( win_count / play_count ) * 100
        print(f"Your win ratio: {win_ratio}%")
        time.sleep(0.5)
        print("\nThanks for playing! Bye!")
        break
