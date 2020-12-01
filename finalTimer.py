import sys ,time ,keyboard

timeout = 5
id = 0
start_time = time.time()
print("Press DEL to enter Setup..........")
while True:
    
    if keyboard.is_pressed("del"):
        id = 1
        print("Break")
        break
    if id == 0 and (time.time() - start_time) > timeout:
        print("timing out, using default value.")
        break
    elif id == 0 and (time.time() - start_time) < timeout:
        #print(".")
        if id == 0 and (time.time() - start_time) == 1:
            print("4")
        if id == 0 and (time.time() - start_time) == 2:
            print("3")
        if id == 0 and (time.time() - start_time) == 3:
            print("2")
        if id == 0 and (time.time() - start_time) == 4:
            print("1")

time.sleep(0.5)