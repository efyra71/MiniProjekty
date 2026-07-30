import datetime
import time
import pygame

def alarm_set():
    alarm_set_time = input("Enter your alarm time: (HH:MM:SS): ")
    print(f"\nAlarm set for {alarm_set_time}\n")
    alarm_working = True

    print("Current time is:")
    while alarm_working:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)

        if current_time == alarm_set_time:
            print("WAKE UP!")
            pygame.mixer.init()
            pygame.mixer.music.load("alarm.mp3")
            pygame.mixer.music.play(-1)
            alarm_working = False
            while True:
                awake = input("Hit Enter if you are awake: ")
                if awake == "":
                    pygame.mixer.music.stop()
                    break
                else:
                    continue


choice = input("Do you want to set an alarm? (Y/N): ").upper()
match choice:
    case "Y":
        alarm_set()
    case "N":
        quit()





