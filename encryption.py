from time import sleep
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         '!', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'Z', '@', '&', '$', '#']
listEncryption = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c',
                  'b', 'a', ' ', '!', 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G',
                  'F', 'E', 'D', 'C', 'B', 'A', '&', '@', '#', '$']
def encrypt(password):
    encryptedMessage = ""
    for char in password:
        characterIndex = chars.index(char)
        encryptedMessage+=listEncryption[characterIndex]
    return encryptedMessage
def decrypt(password):
    decryptedMessage = ""
    for char in password:
        characterIndex = listEncryption.index(char)
        decryptedMessage+=chars[characterIndex]
    return decryptedMessage
def savePassword(ePassword):
    with open('passwords.txt', 'a') as file:
        file.write(f"\nEncrypted password: {ePassword}")
        file.close()
def menu():
    password = input("Enter the password: ")
    password = encrypt(password)
    savePassword(password)
    sleep(3)
    enPassword = input("Enter you encrypted password: ")
    enPassword = decrypt(enPassword)
    print(f"Your password decrypted is: {enPassword}")
    menu()
menu()