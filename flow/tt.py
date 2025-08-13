import time

for j in range (3):
    for i in range (3):
        print (i+j, end='')
    time.sleep(0.5)
    print ("")

print (f"\r\033[3A", end ="")

for j in range (3):
    for i in range (3):
        print (i+j, end='')
    time.sleep(0.5)
    print ("")
