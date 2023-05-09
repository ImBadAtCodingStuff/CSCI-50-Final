# This is a script to generate a password for the user to use for one of there accounts
import random

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


length = int(input("How long would you like the password: "))

def generate(length):
    password = ""
    for i in range(length):
        password+=random.choice(chars)
    print(password)

generate(length)