from time import sleep
import os

# This is the character set for the program to base its knowlege of the alphabet after
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         '!', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'Z', '@', '&', '$', '#']
# This is the reverse of the character set allowing the program to flip each char in the password to a diffrent one and then back
listEncryption = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c',
                  'b', 'a', ' ', '!', 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G',
                  'F', 'E', 'D', 'C', 'B', 'A', '&', '@', '#', '$']
# This method takes in a password from the user and encrypts it
def encrypt(password):
    encryptedMessage = ""
    for char in password:
        characterIndex = chars.index(char)
        encryptedMessage+=listEncryption[characterIndex]
    return encryptedMessage
# This method takes in an encrypted password from the user and return the decrypted version of the password
def decrypt(password):
    decryptedMessage = ""
    for char in password:
        characterIndex = listEncryption.index(char)
        decryptedMessage+=chars[characterIndex]
    return decryptedMessage
# This method checks if the database directory and file is in the right location
# If it is not there it creates the direcotry and the file
def dataBaseDirectory():
    # This method checks if the DataBase directory exists
    def checkPath():
        pathExists = os.path.exists('DataBase')
        if (pathExists):
            print("Found the DataBase directory!")
        else:
            os.mkdir("DataBase")
    # This method checks if the DataBase file exists
    def checkFile():
        fileExists = os.path.isfile('DataBase/myDataBase.txt')
        if (fileExists):
            pass
        else:
            with open('DataBase/myDataBase.txt', 'a') as file:
                file.write("")
    checkPath()
    checkFile()
# This method Writes the encrypted password to the databse file
def savePassword(ePassword):
    with open('DataBase/myDataBase.txt', 'a') as file:
        file.write(f"\nEncrypted password: {ePassword}")
        file.close()
# This is the main method for the script, It is the loop that runs the program for the user
def menu():
    password = input("Enter the password: ")
    password = encrypt(password)
    savePassword(password)
    sleep(3)
    enPassword = input("Enter you encrypted password: ")
    enPassword = decrypt(enPassword)
    print(f"Your password decrypted is: {enPassword}")
    menu()
dataBaseDirectory()
menu()