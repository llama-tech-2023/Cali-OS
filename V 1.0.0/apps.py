import mainSettings as setting
import time
import id
import os 

print("Your installed apps are:")
print("[1] App Installer")
appOption = input("Enter your selection here: ")

if appOption == 1:
    print("Loading app installer...")
    time.sleep(1)
    os.system("python appInstaller.py")
else:
    print("That is not a valid option!")
    retry = input("[1] Try again, [2] close")
    if retry == 1:
        os.system("python apps.py")
    elif retry == 2:
        os.system("python desktop.py")
    else:
        print("Not a valid option!")
        print("Closing app...")
        os.system("python desktop.py")