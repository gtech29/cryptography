# console_app.py
import os
from crypto_core import *


# ==============================
# Input Validation Helpers
# ==============================
def get_mode():
    while True:
        mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
        if mode in ["encrypt", "decrypt"]:
            return mode
        print("Invalid choice. Please type 'encrypt' or 'decrypt'.")


def get_cipher():
    while True:
        cipher = input("Choose cipher (caesar/xor): ").strip().lower()
        if cipher in ["caesar", "xor"]:
            return cipher
        print("Invalid choice. Please type 'caesar' or 'xor'.")


def get_key(cipher):
    while True:
        key = input("Enter key: ").strip()
        if cipher == "caesar":
            if key.isdigit():
                return int(key)
            print("For Caesar cipher, key must be an integer.")
        else:
            if key.isdigit():  # Keep XOR key as integer for simplicity
                return int(key)
            print("For XOR cipher, key must be an integer.")


def get_file_path():
    while True:
        path = input("Enter file path: ").strip()
        if os.path.isfile(path):
            return path
        print("File not found. Try again.")


# ==============================
# Main Program
# ==============================
def main():
    print("\n=== File Encryption Tool ===\n")

    # Get user inputs
    mode = get_mode()
    cipher = get_cipher()
    key = get_key(cipher)
    file_path = get_file_path()

    # Read file
    file_content = read_file(file_path)
    if file_content is None:
        print("Error: Could not read file.")
        return

    # Process content
    if cipher == "caesar":
        result = (
            caesar_encrypt(file_content, key)
            if mode == "encrypt"
            else caesar_decrypt(file_content, key)
        )
    elif cipher == "xor":
        result = (
            xor_encrypt(file_content, key)
            if mode == "encrypt"
            else xor_decrypt(file_content, key)
        )

    # Save result
    write_file(file_path, result, mode)


if __name__ == "__main__":
    main()
