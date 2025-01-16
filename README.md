# Secure Communication System

This repository contains the implementation of a secure communication system for the **CS4600 Final Project**. The system ensures confidentiality, integrity, and authenticity of messages exchanged between a sender and receiver using cryptographic algorithms.

## 📂 File Architecture

- **Sender.py**: Encrypts plaintext messages and sends encrypted data.
- **Receiver.py**: Decrypts the received data and verifies integrity.
- **keygen.py**: Generates RSA key pairs and sets up necessary directories.
- **Sender Directory**: Contains the sender’s keys and plaintext message (`message.txt`).
- **Receiver Directory**: Contains the receiver’s keys and decrypted message (`received_message.txt`).
- **Transmitted_Data**: Simulates a communication channel, storing encrypted messages, keys, and authentication codes.

_Note_: If any required directories or files are missing or modified, running `keygen.py` will recreate them.

## 🔧 How to Use

1. **Download and Extract**:
   - Clone the repository or download the zip file:
     ```bash
     git clone https://github.com/KhaledKorfali2/cs4600_FinalProj.git
     ```
   - Extract the contents to your preferred location.

2. **Generate Keys**:
   - Run `keygen.py` to generate RSA keys and set up the directory structure:
     ```bash
     python keygen.py
     ```

3. **Encrypt and Send Message**:
   - Edit the plaintext message in `Sender/message.txt`.
   - Run `Sender.py` to encrypt the message and write it to `Transmitted_Data`:
     ```bash
     python Sender.py
     ```

4. **Decrypt and Verify Message**:
   - Run `Receiver.py` to decrypt the message and verify integrity:
     ```bash
     python Receiver.py
     ```
   - Check the decrypted message in `Receiver/received_message.txt`.

5. **Repeat (Optional)**:
   - Modify `Sender/message.txt` for a new message and repeat steps 3–4.

## 📖 System Overview

- **Programming Language**: Python (uses the `cryptodome` library).
- **Cryptographic Algorithms**:
  - RSA (2048-bit keys) for key exchange.
  - AES (128-bit keys) for message encryption.
  - SHA-256 for HMAC to ensure message integrity.
  - PKCS1_OAEP padding for secure RSA encryption.

- **Transmitted_Data Structure**:
  - First 256 bytes: Encrypted AES key.
  - Next 16 bytes: Nonce for AES.
  - Next 16 bytes: Authentication tag.
  - Remaining bytes: Ciphertext.
  - Last 32 bytes: HMAC.

## 🛠 Features

- Ensures secure communication using industry-standard cryptographic algorithms.
- Simulates communication via local file storage.
- Simple and modular Python code for ease of understanding.

## 📝 Notes

- Running `keygen.py` resets the `Sender` and `Receiver` directories and overwrites the keys.
- The HMAC verification detects any tampering with the transmitted data.
