import id
import os
import time
import random

#test variables
testConnectionWizard = 0

#welcome stuff
print("Welcome to the setup Wizard!")
print("At any option you can select [0] to exit the wizard.")

confirmContinue = input("Would you like to continue [1] yes or [2] no: ")

time1 = random.uniform(0,1)
time2 = random.uniform(0,1)
time3 = time1 * time2
time4 = random.uniform(0,1)
delayTime = time3 * 2

#universal exit
if confirmContinue == 0:
    print("Exiting...")
    time.sleep(delayTime)
    os.system("python desktop.py")

#exit
elif confirmContinue == 2:
    print("Exiting...")
    time.sleep(delayTime)
    os.system("python desktop.py")

#start setup file
elif confirmContinue == 1:
    print("Now choosing the setup file...")
    time.sleep(delayTime / time4)
    rawSetupFile = input("Enter the setup file name here: ")
    setupFile = str(rawSetupFile)
    time.sleep(delayTime)
    os.system("python " + setupFile)

#error
else:
    print("That is not a valid option!")
    time.sleep(delayTime)
    os.system("python setupWizard.py")