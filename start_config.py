# handle configuration file
import os

# needs work !!!
def get_version():
    with open("config.data", "r") as config_file:
        for line in config_file:
            if (line.startswith("v")):
                versionnum = line[9]+line[10]+line[11]
                # print("This programs version number is: "+versionnum)
                return versionnum

# needs work !!!    
def set_new_main_password(newPassword):
    with open("config.data") as config_file:
        config_file.write("version: "+get_version+"\nmain_password: "+input("Enter a new main password: "))

def first_run():
    firstrun = True
    return firstrun

def read_password_line():
    with open("config.data", "r") as config_file:
        for line in config_file:
            if line.startswith("m"):
                password = line
    return password

def guess_password():
    password = read_password_line()
    guesscount = 0
    while guesscount<3:
        userguess = input("Enter your password: ")
        if ("main_password: "+userguess == password):
            return True
        else:
            print("Wrong password!\n")
    return False
        
# check if config file exists
if (os.path.exists("config.data")):
    print("Path exists")
else:
    print("No config file found...")

if (first_run):
    # ask to set a main password
    set_new_main_password("newpasswordforme")
else:
    # ask the user for there password
    if (guess_password()):
        print("You have access to the software")
    else:
        print("Please restart the application and try again...")
        exit()

            