# -----------------------------------------------------------------------------------------
#
# Program:      CRYPTO - A encryption program based on the Vigenere Cipher
#
# Author:       Hasan Abdulhamid
#
# Description:  Cryto is a command-line program. It prompts the user to enter text
#               to be encrypted. The user will then be prompted to enter an encryption key.
#               Crypto will return the text, encrypted based on the Vigenere Cipher.
#
# -----------------------------------------------------------------------------------------


from helpers import alphabet_position, rotate_character, sym

def encrypt(text, key):
    index = 0
    result = ''
    for char in text:
        if index > (len(key) - 1):
            index = 0
        if char in sym:
            result += char
        else:
            result += rotate_character(char, alphabet_position(key[index]))
            index += 1
    return result


def main():
    message = input("Type a message: ")
    print(message)
    key = input("Encryption key: ")
    print(encrypt(message, key))


if __name__ == "__main__":
    main()
