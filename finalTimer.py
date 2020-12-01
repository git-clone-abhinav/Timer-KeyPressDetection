import sys ,time ,keyboard ,os

timeout = 5
id = 0
start_time = time.time()

while True:
    
    if keyboard.is_pressed("del"):
        #id = 1
        print("Break")
        break
    if id == 0 and (time.time() - start_time) > timeout:
        print("timing out, using default value.")
        break
    else:
        if id == 0 and (time.time() - start_time) > 1:
            print("Press DEL to enter Setup..........")
            print("4")
            id = 1
        if id == 1 and (time.time() - start_time) > 2:
            print("Press DEL to enter Setup..........")
            print("3")
            id = 2
        if id == 2 and (time.time() - start_time) > 3:
            print("Press DEL to enter Setup..........")
            print("2")
            id = 3
        if id == 3 and (time.time() - start_time) > 4:
            print("Press DEL to enter Setup..........")
            print("1")
            id = 4
    time.sleep(1)
    os.system("cls")
    