import time

timeout=10

for i in range(timeout):
    print("time remaining = ",timeout-i)
    time.sleep(1)
    

print("Time is UP")