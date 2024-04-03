# Author: Abraham Moya Gómez

# This is a simple python script that aims to encrypt and decrypt files with a key to protect sensitive data

import colorama
colorama.init()
from cryptography.fernet import Fernet
import os

from colorama import Fore, Style

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt_file(file_name, key):
    cipher = Fernet(key)
    with open(file_name, "rb") as original_file:
        original_data = original_file.read()
    encrypted_data = cipher.encrypt(original_data)
    with open(file_name + ".encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_file(file_name, key):
    cipher = Fernet(key)
    with open(file_name, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(file_name[:-10], "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

def main():
    option = input(f"\n{Fore.BLUE}What do you want to do? (encrypt, decrypt): {Style.RESET_ALL}\n").lower()
    if option == "encrypt":
        file = input(f"\n{Fore.BLUE}Enter the name of the file to encrypt: {Style.RESET_ALL}\n")
        if os.path.exists(file):
            encrypt_file(file, key)
            print(f"\n{Fore.GREEN}File '{file}' encrypted successfully. {Style.RESET_ALL}\n")
            print("Saved to "+file +".encrypted\n")
            remove = input(f"{Fore.YELLOW}Do you want to remove the original file?(y,n) {Style.RESET_ALL}\n")
            if remove == "y":
                os.remove(file)
                print(f"{Fore.GREEN}File '{file}' was succesfully deleted {Style.RESET_ALL}\n")
            elif remove == "n":
                print(f"{Fore.WHITE}Okay, let's keep the original file {Style.RESET_ALL}\n")
            else:
                print(f"{Fore.RED}There was a problem, try again {Style.RESET_ALL}\n")
        else:
            print(f"\n{Fore.RED}The file '{file}' does not exist. {Style.RESET_ALL}\n")
    elif option == "decrypt":
        file = input(f"\n{Fore.BLUE}Enter the name of the file to decrypt: {Style.RESET_ALL}\n")
        if os.path.exists(file):
            decrypt_file(file, key)
            print(f"\n{Fore.GREEN}File '{file}' decrypted successfully. {Style.RESET_ALL}\n")
        else:
            print(f"\n{Fore.RED}The file '{file}' does not exist. {Style.RESET_ALL}\n")
    else:
        print(f"\n{Fore.RED}Invalid option. {Style.RESET_ALL}\n")

if not os.path.exists("key.key"):
    generate_key()

key = load_key()

main()