import sys ,time ,keyboard ,os

timeout = 5
id = 0
seconds = 10

start_time = time.time()

while True:
    if keyboard.is_pressed("enter"):
        id = 1
        print("Break")
        break
    if id == 0 and (time.time() - start_time) > timeout:
        print("timing out, using default value.")
        break
        



def loading_screen():
    with open('ccnet.txt', 'r') as screen:
        for lines in screen:
            print(lines, end='')

def loading_bar(seconds):
    for loading in range(0, seconds+1):
        print("\n")
        print("Press Enter to enter Setup")
        print("<" + ("✈ " * loading) + ("" * (seconds + loading)) +">")
        print("\n")
        waiting_keypress(seconds)

'''def waiting_keypress(seconds):
        
    for loading in range(0,seconds+1):
        
        if keyboard.is_pressed("enter"):
            id=1
            os.system('cls' if os.name == "nt" else "clear")
            break
            os.system('cls' if os.name == "nt" else "clear")

        time.sleep(1)'''
        


#loading_screen()
#loading_bar(seconds)

'''if(id==1):
    print("Entering CCThinClient Setup")
elif(id==0):
    print("Loading Client ..")
'''