# socket_client.py
import socket
from crypto_core import *


def main():
    host = "127.0.0.1"  # Server IP (localhost for testing)
    port = 65432  # Must match server port

    message = input("Enter message: ")
    cipher = input("Choose cipher (caesar/xor): ").strip().lower()
    key = input("Enter key: ").strip()

    if not key.isdigit():
        print("Key must be an integer.")
        return
    key = int(key)

    # Encrypt based on chosen cipher
    if cipher == "caesar":
        encrypted = caesar_encrypt(message, key)
    elif cipher == "xor":
        encrypted = xor_encrypt(message, key)
    else:
        print("Invalid cipher choice.")
        return

    # Prepare data in format: cipher|key|encrypted
    data_to_send = f"{cipher}|{key}|{encrypted}"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(data_to_send.encode("utf-8"))
        print(f"Encrypted message sent: {encrypted}")

        # Wait for confirmation from server
        confirmation = s.recv(1024).decode("utf-8")
        print(f"Server confirmation: {confirmation}")


if __name__ == "__main__":
    main()
