# console_app.py
import os
from crypto_core import *


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
            # For XOR, you can allow either int or string key
            if key:
                return key
            print("Key cannot be empty.")


def get_file_path():
    while True:
        path = input("Enter file path: ").strip()
        if os.path.isfile(path):
            return path
        print("File not found. Try again.")


def main():
    print("\n=== Encryption Tool ===\n")
    mode = get_mode()
    cipher = get_cipher()
    key = get_key(cipher)
    file_path = get_file_path()

    print(f"\nMode: {mode}")
    print(f"Cipher: {cipher}")
    print(f"Key: {key}")
    print(f"File: {file_path}")


if __name__ == "__main__":
    main()
