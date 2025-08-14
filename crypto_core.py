# crypto_core.py
import os


# ==============================
# File Handling
# ==============================
def read_file(file_path):
    """Read and return the contents of a text file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def write_file(file_path, data, mode):
    """
    Write data to a new file.
    If mode == 'encrypt', save as .enc.
    If mode == 'decrypt', save as .txt.
    """
    try:
        base_name, _ = os.path.splitext(file_path)  # remove old extension
        if mode == "encrypt":
            new_path = base_name + ".enc"
        elif mode == "decrypt":
            new_path = base_name + ".txt"
        else:
            print("Invalid mode for writing file.")
            return None

        with open(new_path, "w", encoding="utf-8") as f:
            f.write(data)

        print(f"File saved as: {new_path}")
        return new_path
    except Exception as e:
        print(f"Error writing file: {e}")
        return None


# ==============================
# Caesar Cipher
# ==============================
def caesar_encrypt(text, key):
    """Encrypt text using Caesar cipher."""
    result = ""
    for char in text:
        if char.isalpha():
            shift = key % 26  # keep within alphabet range
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def caesar_decrypt(text, key):
    """Decrypt text using Caesar cipher."""
    return caesar_encrypt(text, -key)  # reverse shift


# ==============================
# XOR Cipher
# ==============================
def xor_encrypt(text, key):
    """Encrypt text using XOR cipher with an integer key."""
    result_chars = []
    for char in text:
        result_chars.append(chr(ord(char) ^ key))
    return "".join(result_chars)


def xor_decrypt(text, key):
    """Decrypt text using XOR cipher (same as encryption)."""
    return xor_encrypt(text, key)
