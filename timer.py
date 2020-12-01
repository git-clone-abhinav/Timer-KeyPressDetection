import time
import keyboard
import os
seconds = 10
id = 0

def loading_screen():
    with open('ccnet.txt', 'r') as screen:
        for lines in screen:
            print(lines, end='')

def loading_bar(seconds):
    for loading in range(0, seconds+1):
        
        if keyboard.is_pressed("enter"):
            id=1
            time.sleep(1)
            print("Pressed")
            break
        else:
            id=0
            time.sleep(0)
            print("Not Pressed")


loading_screen()
loading_bar(seconds)

if(id==1):
    print("Entering CCThinClient Setup")
elif(id==0):
    print("Loading Client ..")
