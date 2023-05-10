# This is a script to generate a password for the user to use for one of there accounts
import random
import sqlite3

# setup for connecting to the databse
databseconnection=sqlite3.connect("PasswordSquirrel.db")
cursor=databseconnection.cursor()

# chars
chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
         "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
         "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "~", "<", ">", "?", "/", "{", "}", "\\", "|", "[", "]", "_",
         "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# ask for length
# for length
# generate a random charecter
# add it to a string
# display the password

def save_to_database(username, password):
    cursor.execute(f"""INSERT INTO accounts VALUES ('{username}', '{password}')""")
    databseconnection.commit()
    if (cursor.execute(f"""SELECT * FROM account WHERE username='{username}'""") is not None):
        print("Account data saved sucessfully...")



def generate(length):
    password = ""
    for i in range(length):
        password+=random.choice(chars)
    return password

def main():
    while 1:
        password=generate(int(input("Password length: ")))
        if (input("Do you like: "+password+" as your password: (y/n) ")=="y"):
            save_to_database(input("Enter the username for the account: "), password)
        else:
            print("Lets try another one")

main()