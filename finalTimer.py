import sys ,time ,keyboard

timeout = 5
id = 0
start_time = time.time()

while True:
    if keyboard.is_pressed("enter"):
        id = 1
        print("Break")
        break
    if id == 0 and (time.time() - start_time) > timeout:
        print("timing out, using default value.")
        break