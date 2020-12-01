import time
import threading

def do_something():
    T0 = time.clock()
    while (time.clock() - T0) < 60 and not e.isSet(): #as long as 60s haven't elapsed
                                                      #and the flag is not set
        #here do a bunch of stuff
        time.sleep(5)

thread = threading.Thread(target=do_something, args=())
e = threading.Event()
thread.start()

print("Press CTRL-C to interrupt")
while thread.isAlive():
    try: time.sleep(1) #wait 1 second, then go back and ask if thread is still alive
    except KeyboardInterrupt: #if ctrl-C is pressed within that second,
                              #catch the KeyboardInterrupt exception
        e.set() #set the flag that will kill the thread when it has finished
        print("Exiting")
        thread.join() #wait for the thread to finish