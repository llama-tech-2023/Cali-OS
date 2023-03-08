import mainSettings as setting
import listOfCommands as command
import random
import users
import cpu
import ram
import os
import time

print("Starting terminal...")

time1 = random.uniform(0,1)
time2 = random.uniform(0,1)
time3 = time1 * time2
delayTime = time3 * 2

time.sleep(delayTime)
print("Welcome to the Cali terminal")

ram.command = str(input("root@Cali $ ~: "))


#command processing
if ram.command == "exit": #exit the program and go to the desktop
    cpu.terminalUserPath()
    time.sleep(1)
    print("Exiting terminal...")
    time.sleep(0.75)
    os.system("python desktop.py")

elif ram.command == "cd": #normal cd command
    command.cd = setting.true
    cpu.terminalUserPath()

elif ram.command == "cd..": #back one directory cd command
    cpu.terminalUserPath()
    command.cdBackDir = setting.true

elif ram.command == "cd dir": #checks if the prompt wants a directory input
    cpu.terminalUserPath()
    command.cdDir = setting.true
    ram.chosenDir = str(input("Enter the directory you want to enter into: "))

elif ram.command == "sudo": #checks for a sudo command

    ram.sudoCommandModifier = input(str(">: ")) #opens input for the command modifier
    time.sleep(delayTime)

    print(ram.sudoCommandModifier)

elif ram.command == "exit":
    print("exiting...")
    time.sleep(delayTime)
    os.system("python desktop.py")

else:
    print("That is not a valid command!")
    print("Type [?] for help or a list of commands")