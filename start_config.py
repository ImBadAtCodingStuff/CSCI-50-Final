# main developer of this script: Evan White

# this script manages the first run condition of the program

# handle configuration file
import os
import sqlite3
import subprocess

# setup for connecting to the databse
databseconnection=sqlite3.connect("PasswordSquirrel.db")
cursor=databseconnection.cursor()

# needs work !!!
def get_version():
    with open("config.data", "r") as config_file:
        for line in config_file:
            if (line.startswith("v")):
                versionnum = line[9]+line[10]+line[11]
                # print("This programs version number is: "+versionnum)
                return versionnum

# needs work !!!    
def set_new_main_password():
    with open("config.data", "w") as config_file:
        config_file.write("version: "+"0.1"+"\nmain_password: "+input("Enter a new main password: "))

def first_run():
    # check if config file exists
    if (os.path.exists("config.data")):
        print("Path exists")
        firstrun = False
    else:
        print("No config file found...")
        firstrun = True
    return firstrun

def read_password_line():
    with open("config.data", "r") as config_file:
        for line in config_file:
            if line.startswith("m"):
                password = line
    return password

def create_table():
    cursor.execute("""CREATE TABLE Password_Data (Service varchar(30) PRIMARY KEY, Username varchar(30), Password varchar(30))""")
    databseconnection.commit()


def guess_password():
    password = read_password_line()
    guesscount = 0
    while guesscount<3:
        userguess = input("Enter your password: ")
        if ("main_password: "+userguess == password):
            return True
        else:
            print("Wrong password!\n")
            guesscount+=1
        print("You have guessed "+str(guesscount)+" times...")
    return False


if (first_run()):
    # ask to set a main password
    set_new_main_password()
    create_table()
else:
    # ask the user for there password
    if (guess_password()):
        print("You have access to the software")
    else:
        print("Please restart the application and try again...")
        exit()

subprocess.call(['./MainMenuSelect.sh'])
            