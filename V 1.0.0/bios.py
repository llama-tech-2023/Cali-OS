from zipfile import ZipFile
import os
import time

biosVersion = str("1.0")

print("Powering on...")
time.sleep(1)
option = input("You can either [1] boot, [2] update, [3] shutdown, or [4] display version of the bios: ")

if option == 4:
    print("Bios is version " + biosVersion)
    time.sleep(0.5)
    os.system("python bios.py")
elif option == 3:
    print("Powering off...")
    time.sleep(1)
    exit()
elif option == 2:
    print("Getting ready for update...")
    print("Bios is version " + biosVersion)
    continueConfirm = input("Do you want to continue? [1] yes, [2] no: ")
    
    if continueConfirm == 2:
        os.system("python bios.py")

    elif continueConfirm == 1:
        #move the zip file to the main pc
        #os.system("sudo mv /home/kaylee/Cali/Downloads/biosUpdate.zip /home/kaylee/Cali/ThisPC/")

        #extract the files
        with ZipFile("/home/kaylee/Cali/Downloads/biosUpdate.zip", 'r') as zObject:
  
        # Extracting all the members of the zip 
        # into a specific location.
            zObject.extractall(path="/home/kaylee/Cali/ThisPC")

        #this finds files with a specific extention
        for root, dirs, files in os.walk("/home/kaylee/Cali/ThisPC"):
            for file in files:
                if file.endswith(".bios"):
                    os.system("sudo mv biosupdate.bios biosupdate.py")
                    os.system("python biosupdate.py")
elif option == 1:
    print("Powering on...")
    time.sleep(0.5)
    os.system("python boot.py")