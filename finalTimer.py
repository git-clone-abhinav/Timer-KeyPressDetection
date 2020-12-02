import time, keyboard, os
from module import *

timeout = 5
id = 0
start_time = time.time()

print("Press DEL to enter Setup..........")

while True:
    
    if keyboard.is_pressed("del"):
        print_break()
        break
    if id == 0 and (time.time() - start_time) > timeout:
        #os.system("startx")
        print("startx")
        break
    #time.sleep(1)
    #os.system("cls")
    