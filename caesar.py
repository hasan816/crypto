# -----------------------------------------------------------------------------------------
#
# Program:      CRYPTO - A encryption program based on the Caesar Cipher
#
# Author:       Hasan Abdulhamid
#
# Description:  Cryto is a command-line program. It prompts the user to enter text
#               to be encrypted. The user will then be prompted to enter an encryption key.
#               Crypto will return the text, encrypted based on the Caesar Cipher.
#
# File:         caesar.py - This file contains the main method for the Crypto
#
# -----------------------------------------------------------------------------------------


from helpers import rotate_character


def encrypt(text, rot):
    result = ''
    for item in text:
        result += rotate_character(item, rot)
    return result


def main():
    message = input("Type a message: ")
    print(message)
    rotate = int(input("Rotate by: "))
    print(encrypt(message, rotate))


if __name__ == "__main__":
    main()



