# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:22:22 2023

@author: khale
"""
import os
import sys
import hashlib
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util import Counter, Padding

# Read receiver's private key
with open('receiver_private_key.pem', 'rb') as f:
    receiver_private_key = RSA.import_key(f.read())

# Read sender's encrypted data
with open('Transmitted_Data', 'rb') as f:
    all_Transmitted_Data = f.read()
    data_size = all_Transmitted_Data.__len__()
    #print(data_size)
    f.seek(0)
    encrypted_aes_key = f.read(256)
    nonce = f.read(16)
    tag = f.read(16)
    ciphertext = f.read(data_size-256-16-16-32)
    mac = f.read(32)


try:
    # Decrypt AES key with receiver's private key
    cipher_rsa = PKCS1_OAEP.new(receiver_private_key)
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)

    # Generate HMAC of received data and compare to transmitted HMAC
    key = hashlib.sha256(aes_key).digest()
    h = hashlib.sha256()
    h.update(ciphertext)
    h.update(tag)
    
    if not h.digest() == mac:
        print("Data corrupted! HMAC does not match.")
        sys.exit(1)
    
    # Decrypt message with AES key
    cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce)
    plaintext = cipher_aes.decrypt_and_verify(ciphertext, tag)
    
    # Write decrypted message to a file
    with open('received_message.txt', 'wb') as f:
        f.write(plaintext)
    
    print("Message received and saved to file!")
    sys.exit(0)
except SystemExit:
    pass  # ignore the SystemExit exception and continue executing
except:
    print("Warning Data Has Been Currupted!")
    sys.exit(1)


