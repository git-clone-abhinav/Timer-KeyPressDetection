import time
import keyboard
import os
seconds = 5

def loading_screen():
    with open('ccnet.txt', 'r') as screen:
        for lines in screen:
            print(lines, end='')

def loading_bar(seconds):
    for loading in range(0, seconds+1):
        percent = (loading * 100) // seconds
        print("\n")
        print("Press Enter to enter Setup")
        print("<" + ("-" * loading) + ("" * (seconds + loading)) +">" + str(percent) + "%")
        print("\n")
        time.sleep(1)
        os.system('cls' if os.name == "nt" else "clear")
        loading_screen()


loading_screen()
loading_bar(seconds)

'''for i in range(timeout):
    print("time remaining = ",timeout-i)
    time.sleep(1)
    if keyboard.is_pressed("enter"):
        break'''
