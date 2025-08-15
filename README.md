# File Encryption Tool with Caesar & XOR Ciphers

## Overview
This project is a file-based encryption and decryption tool implemented in Python.  
It supports two classical ciphers:
- **Caesar Cipher**
- **XOR Cipher**

It includes:
1. **Console Application** for encrypting and decrypting text files.
2. **Socket Programming Bonus** for encrypted client-server communication.

---

## Features
- Encrypt and decrypt text files.
- Support for **Caesar Cipher** and **XOR Cipher**.
- User-friendly input validation.
- Save encrypted files with `.enc` extension.
- Save decrypted files with `.txt` extension.
- **Bonus**: TCP socket client and server for sending encrypted messages.

---

## File Structure
```
encryption_tool/
│
├── crypto_core.py        # Core cipher logic and file handling
├── console_app.py        # Main CLI tool
├── socket_client.py      # Bonus: sends encrypted message to server
├── socket_server.py      # Bonus: receives and decrypts message
└── README.md             # This file
```

---

## Requirements
- Python 3.8+
- No external dependencies (uses only built-in Python libraries)

---

## How to Run

### 1. Console Application
```bash
python console_app.py
```
Follow the prompts:
1. Choose `encrypt` or `decrypt`.
2. Choose cipher: `caesar` or `xor`.
3. Enter a key:
   - **Caesar**: integer
   - **XOR**: integer
4. Enter the file path.
5. The output will be saved with `.enc` (encrypted) or `.txt` (decrypted).

---

### 2. Socket Bonus (Encrypted Communication)
#### Start the Server:
```bash
python socket_server.py
```

#### Start the Client (in another terminal):
```bash
python socket_client.py
```

#### Flow:
1. The client asks for a message, cipher, and key.
2. The message is encrypted and sent to the server.
3. The server decrypts and displays the message.
4. The server sends a confirmation back to the client.

---

## Example (Caesar Cipher)
**Client Input:**
```
Enter message: Hello
Choose cipher (caesar/xor): caesar
Enter key: 3
```

**Server Output:**
```
Encrypted message received: Khoor
Decrypted message: Hello
```

---

## Notes
- Make sure the client and server are using the **same cipher and key** for correct decryption.
- Keys for XOR are integers for simplicity.
- This project works with text files (`.txt`) and plain text messages.

---

## Author
Juan Rodriguez
