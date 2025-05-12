import time

timer=int(input("Set the Timer:"))

for i in range(0,timer):
    clear()
    print(i)
    time.sleep(1)
    
print("TIME'S UP")