# crypto_core.py


# crypto_core.py
import os


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


def caesar_encrypt(text, key):
    """Encrypt text using Caesar cipher."""
    pass


def caesar_decrypt(text, key):
    """Decrypt text using Caesar cipher."""
    pass


def xor_encrypt(text, key):
    """Encrypt text using XOR cipher."""
    pass


def xor_decrypt(text, key):
    """Decrypt text using XOR cipher."""
    pass
