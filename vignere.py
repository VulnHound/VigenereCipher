"""
Vignere Cipher
by: @VulnHound
version 0.1.0
Created: 11/10/2019
"""

from pycipher import *
from pyfiglet import Figlet
import os

# Vigenere Cipher Banner


def banner():
    os.system('clear' or 'cls')
    custom_fig = Figlet(font='cosmic')
    print(custom_fig.renderText('Vigenere Cipher'))
    print("version 0.1.0")
    print("by: @VulnHound")
    print("\n" * 8)


# User Selection Function


def welcome_message():
    print("\n1. Encrypt")
    print("2. Decrypt\n")
    print("\nNeed Help - 'sos'\n")
    print("\n0. Quit\n")
    selection = input("")
    return selection

# Vigenere Grid


def vigenere_grid():
    os.system('clear' or 'cls')
    print("\n" + "-" * 66)
    print("\n\n    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z" + " " * 10 + "#")
    print("    ---------------------------------------------------" + " " * 10 + "#")
    print("A   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z" + " " * 10 + "#")
    print("B   B C D E F G H I J K L M N O P Q R S T U V W X Y Z A" + " " * 10 + "#")
    print("C   C D E F G H I J K L M N O P Q R S T U V W X Y Z A B" + " " * 10 + "#")
    print("D   D E F G H I J K L M N O P Q R S T U V W X Y Z A B C" + " " * 10 + "#")
    print("E   E F G H I J K L M N O P Q R S T U V W X Y Z A B C D" + " " * 10 + "#")
    print("F   F G H I J K L M N O P Q R S T U V W X Y Z A B C D E" + " " * 10 + "#")
    print("G   G H I J K L M N O P Q R S T U V W X Y Z A B C D E F" + " " * 10 + "#")
    print("H   H I J K L M N O P Q R S T U V W X Y Z A B C D E F G" + " " * 10 + "#")
    print("I   I J K L M N O P Q R S T U V W X Y Z A B C D E F G H" + " " * 10 + "#")
    print("J   J K L M N O P Q R S T U V W X Y Z A B C D E F G H I" + " " * 10 + "#")
    print("K   K L M N O P Q R S T U V W X Y Z A B C D E F G H I J" + " " * 10 + "#")
    print("L   L M N O P Q R S T U V W X Y Z A B C D E F G H I J K" + " " * 10 + "#")
    print("M   M N O P Q R S T U V W X Y Z A B C D E F G H I J K L" + " " * 10 + "#")
    print("N   N O P Q R S T U V W X Y Z A B C D E F G H I J K L M" + " " * 10 + "#")
    print("O   O P Q R S T U V W X Y Z A B C D E F G H I J K L M N" + " " * 10 + "#")
    print("P   P Q R S T U V W X Y Z A B C D E F G H I J K L M N O" + " " * 10 + "#")
    print("Q   Q R S T U V W X Y Z A B C D E F G H I J K L M N O P" + " " * 10 + "#")
    print("R   R S T U V W X Y Z A B C D E F G H I J K L M N O P Q" + " " * 10 + "#")
    print("S   S T U V W X Y Z A B C D E F G H I J K L M N O P Q R" + " " * 10 + "#")
    print("T   T U V W X Y Z A B C D E F G H I J K L M N O P Q R S" + " " * 10 + "#")
    print("U   U V W X Y Z A B C D E F G H I J K L M N O P Q R S T" + " " * 10 + "#")
    print("V   V W X Y Z A B C D E F G H I J K L M N O P Q R S T U" + " " * 10 + "#")
    print("W   W X Y Z A B C D E F G H I J K L M N O P Q R S T U V" + " " * 10 + "#")
    print("X   X Y Z A B C D E F G H I J K L M N O P Q R S T U V W" + " " * 10 + "#")
    print("Y   Y Z A B C D E F G H I J K L M N O P Q R S T U V W X" + " " * 10 + "#")
    print("Z   Z A B C D E F G H I J K L M N O P Q R S T U V W X Y" + " " * 10 + "#")


# Print out the banner message

banner()
userSelection = welcome_message()

while userSelection.lower() != "0":

    # If selection for user input

    if userSelection == "1":
        plain = input("\nEnter plain text to encrypt: ")

        key = input("Enter a key 'word' to build the cipher: ")

        ciphertext = Vigenere(key).encipher(plain)

        banner()
        print("\n" + "-" * 30)
        print(ciphertext)
        print("-" * 30)
        userSelection = welcome_message()

    elif userSelection == "2":
        crypt = input("\nEnter in text to decrypt: ")
        key = input("Enter the key 'word' to decrypt the cipher: ")

        plaintext = Vigenere(key).decipher(crypt)

        banner()
        print("\n" + "-" * 30)
        print(plaintext)
        print("-" * 30)
        userSelection = welcome_message()

    elif userSelection == "sos":
        vigenere_grid()
        print("\n" + "-" * 66)
        print("\nThe Vigenère Cipher is a polyalphabetic substitution cipher\n")
        print("First you will enter in the text you want to Encrypt/Decrypt.")
        print("Then to build the cipher you need to provide a 'key word'.")
        print("\nHere's an example:\n")
        print("Your key word:       'vulnhound'\n")
        print("Repeat your key word above your text.\n")
        print("Key word applied:    VULNHOUNDVULNHOUN")
        print("Your message:        ILOVECRYPTOGRAPHY")
        print("\nNow we take the letter we will be encoding, 'I', and find it on the first column.")
        print("Then, we move along the 'I' row of the tableau until we come to the column with the 'V' at the top.")
        print("The intersection is our ciphertext character, 'D'.")
        print("\nThe results become:\n")
        print("Key Word:        VULNHOUNDVULNHOUN")
        print("Your Message:    ILOVECRYPTOGRAPHY")
        print("Ciphertext:      DFZILQLLSOIREHDBL")
        print("\nAND THAT'S IT!\n")
        print("\n" + "-" * 100 + "\n")

        userSelection = welcome_message()

    elif userSelection == "0":
        os.system('clear' or 'cls')
        exit()

    else:
        banner()
        print("\nBad selection...try again.\n")
        userSelection = welcome_message()
