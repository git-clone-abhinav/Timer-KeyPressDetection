import time
import keyboard
timeout=10

for i in range(timeout):
    print("time remaining = ",timeout-i)
    time.sleep(1)
    if keyboard.is_pressed("enter"):
        break


print("Time is UP")