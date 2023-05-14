# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:21:46 2023

@author: khale
"""
import os
import sys
import hashlib
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Util import Counter, Padding


#Define the name of the main director folder
main_dir = os.getcwd()

# Define the name of the subdirectory to read
sender_dir = "Sender"
sender_keys_dir = "Sender_Keys"

# Get the full path of the subdirectory
subdir_path_sender = os.path.join(os.getcwd(), sender_dir)

# Get the full path of the subdirectory
subdir_path_sender_keys = os.path.join(subdir_path_sender, sender_keys_dir)

# Check if the subdirectory exists
if os.path.isdir(subdir_path_sender):
    os.chdir(subdir_path_sender)
else:
    print("Error No Directory {subdir_path_sender}")
   
if os.path.isdir(subdir_path_sender_keys):
    os.chdir(subdir_path_sender_keys)

    # Read the receiver's public key
    with open('receiver_public_key.pem', 'rb') as f:
        receiver_public_key = RSA.import_key(f.read())
    
    # Encrypt AES key with receiver's public key
    aes_key = get_random_bytes(16)
    cipher_rsa = PKCS1_OAEP.new(receiver_public_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)
    
    #Go back to Sender directory folder
    os.chdir(subdir_path_sender)
    
    # Encrypt message with AES key
    with open('message.txt', 'rb') as f:
        plaintext = f.read()
    cipher_aes = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(plaintext)
    
    # Generate HMAC of encrypted data
    key = hashlib.sha256(aes_key).digest()
    h = hashlib.sha256()
    h.update(ciphertext)
    h.update(tag)
    hmac = h.digest()
    
    #Go back to main directory folder
    os.chdir(main_dir)
    
    # Write encrypted data and HMAC to a file
    with open('Transmitted_Data', 'wb') as f:
        f.write(encrypted_aes_key)
        #print(encrypted_aes_key.__len__())
        
        f.write(cipher_aes.nonce)
        #print(cipher_aes.nonce.__len__())
        
        f.write(tag)
        #print(tag.__len__())
       
        f.write(ciphertext)
        #print(ciphertext.__len__())
        
        f.write(hmac)
        #print(hmac.__len__())
    
    print("Message sent!")
    sys.exit(0)
else:
    print("Error No Directory {subdir_path_sender}")
    sys.exit(1)