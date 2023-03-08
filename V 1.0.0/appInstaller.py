import fileExtentions as extention
import random
import time
import os

#define the extentions
update = extention.update
patch = extention.patch

test = None

def quitScript():
    print("Quitting!")
    os.system("python appInstaller.py")

def elseScript():
    os.system("python appInstaller.py")

sleep1 = random.uniform(0,1)
sleep2 = random.uniform(0,1)
timeSleep = (sleep1 * sleep2) * 2

print("App installer loaded!")
print("Starting app installer...")
time.sleep(timeSleep)
print("App installer started successfully!")

continueOption = input("Would you like to continue? [1] yes, [2] no: ")

if continueOption == 2:
    print("Quitting!")
    os.system("python apps.py")
    
elif continueOption == 1:
    print("Initializing software...")
    time.sleep(timeSleep)

    rawFolderName = input("Enter the name of the folder: ")
    rawFileExtention = input("Enter the extention of the setup file without the '.': ")

    #variables for install
    rawFileName = rawFolderName

    folderConfirm = input("Is the folder: " + rawFolderName + " correct? [1] yes, [2] no: ")

    if folderConfirm == 2:
        quitScript()

    elif folderConfirm == 1:
        print("Confirmed!")

        fileConfirm = input("Is the file: " + rawFileName + " correct? [1] yes, [2] no: ")

        if fileConfirm == 2:
          quitScript()

        if fileConfirm == 1:
            print("Confirmed!")

            extentionConfirm = input("Is the file extention " + rawFileExtention + " correct? [1] yes, [2] no: ")
          
            if extentionConfirm == 2:
                quitScript()

            elif extentionConfirm == 1:
                print("Folder, file, and extention confirmed!")

                installConfirm = input("Enter [1] to continue to the installation or [2] Quit: ")

                if installConfirm == 2:
                   quitScript()

                elif installConfirm == 1:
                    print("Starting the install of the new application!")

                    #convert the variables to usable strings that can be ran in a command
                    folderName = str(rawFolderName)
                    fileName = str(rawFileName)
                    fileExtention = str(rawFileExtention)

                    os.system("python " + folderName + fileName + fileExtention)


#if no option is acceptable then restart the app
                else:
                    elseScript()
            else:
               elseScript()
        else:
           elseScript()
    else:
      elseScript()
else:
     elseScript()