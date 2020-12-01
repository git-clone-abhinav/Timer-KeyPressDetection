import time, keyboard, os

timeout = 5
id = 0
start_time = time.time()

def printing_menu():
    print("Press DEL to enter Setup..........")

while True:
    
    if keyboard.is_pressed("del"):
        print("Break")
        break
    if id == 4 and (time.time() - start_time) > timeout:
        print("timing out, using default value.")
        break
    else:
        
        if id == 0 and (time.time() - start_time) > 1:
            printing_menu()
            print("4")
            id = 1
            if keyboard.is_pressed("del"):
                print("Break")
                break
        if id == 1 and (time.time() - start_time) > 2:
            printing_menu()
            print("3")
            id = 2
            if keyboard.is_pressed("del"):
                print("Break")
                break
        if id == 2 and (time.time() - start_time) > 3:
            printing_menu()
            print("2")
            id = 3
            if keyboard.is_pressed("del"):
                print("Break")
                break
        if id == 3 and (time.time() - start_time) > 4:
            printing_menu()
            print("1")
            id = 4
            if keyboard.is_pressed("del"):
                print("Break")
                break
    #time.sleep(1)
    #os.system("cls")
    