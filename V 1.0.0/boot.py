import os
import time
import random

sleep1 = random.uniform(0,1)
sleep2 = random.uniform(0,1)
timeSleep = (sleep1 * sleep2) * 2

print("Booting the Computer...")
time.sleep(timeSleep)

option = input("Would you like to [1] boot the computer or [2] enter the BIOS: ")

if option == 2:
    print("Entering the Bios menu..")
    time.sleep(timeSleep)
    os.system("python bios.py")

elif option == 1:
    print("Booting the computer...")
    time.sleep(timeSleep)
    os.system("python desktop.py")