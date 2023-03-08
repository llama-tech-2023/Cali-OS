import mainSettings as setting
import random
import time
import ram
import os
import id
import cpu

ram.userbypass = setting.false

#initialize things that will be stored in ROM RAM later
User = 'sample'
tryUser = 'sample'

#passwords
test = 'test'
root = 'root'
admin = 'admin'

print("Welcome to Cali!")

if ram.userbypass == setting.false:
    print("List of users:")
    print("[1] root")
    print("[2] Kaylee")
    print("[3] Admin")
    selectedUser = str(input("Enter the user number here: "))

    if selectedUser == 1:
        tryUser = str("root")
    elif selectedUser == 2:
        tryUser = str("Kaylee")
    elif selectedUser == 3:
        tryUser = str("Admin")

    userPassword = None

    #login page for users
    print("Welcome to Cali " + tryUser + "!")
    userPassword = input("Please enter your password: ")

    #make a random delay time
    time1 = random.uniform(0,1)
    time2 = random.uniform(0,1)
    time3 = time1 * time2
    delayTime = time3 * 2

    #check password
    if userPassword == 'root':          #default password
        time.sleep(delayTime)
        print("Welcome " + tryUser + ".")
        User = tryUser
    elif userPassword == 'test':  #default password
        time.sleep(delayTime)
        print("Welcome " + tryUser + ".")
        User = tryUser
    elif userPassword == 'admin':       #default password
        time.sleep(delayTime)
        print("Welcome " + tryUser + ".")
        User = tryUser
    else:
        time.sleep(delayTime)
        print("That password is incorrect!")
        time.sleep(delayTime / 0.75)
        os.system("python desktop.py")
    
    ram.userbypass = setting.true

#apps
print("[1] terminal")
print("[2] apps")
print("[3] settings")
print("[0] logout")
menuOption = input("Enter your option here: ")

if menuOption == 0:
    print()
elif menuOption == 1:
    print("Opening terminal...")
    time.sleep(1)
    print("Done!")
    os.system("python terminal.py")
elif menuOption ==2:
    print("Loading apps menu...")
    time.sleep(0.75)
    os.system("python apps.py")
else:
    print("That is not a valid option!")
