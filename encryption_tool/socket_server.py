# socket_server.py
import socket
from crypto_core import *


def main():
    host = "127.0.0.1"  # Listen locally
    port = 65432  # Must match client port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f"Server listening on {host}:{port}...")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024)
            if not data:
                return

            # Decode and parse: cipher|key|encrypted_message
            decoded_data = data.decode("utf-8")
            cipher, key, encrypted_msg = decoded_data.split("|", 2)
            key = int(key)

            print(f"Cipher: {cipher}")
            print(f"Key: {key}")
            print(f"Encrypted message received: {encrypted_msg}")

            # Decrypt
            if cipher == "caesar":
                decrypted = caesar_decrypt(encrypted_msg, key)
            elif cipher == "xor":
                decrypted = xor_decrypt(encrypted_msg, key)
            else:
                decrypted = "(Unknown cipher type)"

            print(f"Decrypted message: {decrypted}")

            # Send confirmation back to client
            confirmation = f"Message received and decrypted: {decrypted}"
            conn.sendall(confirmation.encode("utf-8"))


if __name__ == "__main__":
    main()
