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
# File:         helpers.py - This file contains helper modules for vigenere.py
#
# -----------------------------------------------------------------------------------------


import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
sym = string.punctuation + string.digits + ' '


def alphabet_position(letter):
    return lower.find(letter.lower())


def rotate_character(char, rot):
    result = ''
    if char in sym:
        return char
    indx = alphabet_position(char) + rot
    if indx > 25:
        indx = indx % 26
    if char in upper:
        result = upper[indx]
    elif char in lower:
        result = lower[indx]
    return result
