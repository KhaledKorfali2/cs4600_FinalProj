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


#Define the name of the main director folder
main_dir = os.getcwd()

# Define the name of the subdirectory to read
receiver_dir = "Receiver"
receiver_keys_dir = "Receiver_Keys"

# Get the full path of the subdirectory
subdir_path_receiver = os.path.join(os.getcwd(), receiver_dir)

# Get the full path of the subdirectory
subdir_path_receiver_keys = os.path.join(subdir_path_receiver, receiver_keys_dir)

# Check if the subdirectory exists
if os.path.isdir(subdir_path_receiver):
    os.chdir(subdir_path_receiver)  # Change the current working directory to the receiver subdirectory
else:
    print("Error No Directory {subdir_path_receiver}")
    

# Check if the subdirectory exists
if os.path.isdir(subdir_path_receiver_keys):
    os.chdir(subdir_path_receiver_keys)  # Change the current working directory to the receiver keys subdirectory
    
    # Read receiver's private key
    with open('receiver_private_key.pem', 'rb') as f:
        receiver_private_key = RSA.import_key(f.read())  # Import the receiver's private key
    
    #Go back to main directory folder
    os.chdir(main_dir)
    
    # Read sender's encrypted data
    with open('Transmitted_Data', 'rb') as f:
        all_Transmitted_Data = f.read()  # Read the entire transmitted data
        data_size = all_Transmitted_Data.__len__()   # Get the size of the transmitted data
        #print(data_size)
        f.seek(0)  # Move the file pointer to the beginning of the file
        encrypted_aes_key = f.read(256)  # Read the encrypted AES key
        nonce = f.read(16)  # Read the nonce used by AES
        tag = f.read(16)  # Read the tag
        ciphertext = f.read(data_size-256-16-16-32)  # Read the ciphertext
        mac = f.read(32)  # Read the MAC (HMAC)
    
    
    try:
        # Decrypt AES key with receiver's private key
        cipher_rsa = PKCS1_OAEP.new(receiver_private_key)  # Create an RSA cipher object for decryption
        aes_key = cipher_rsa.decrypt(encrypted_aes_key) # Decrypt the AES key using the receiver's private key
    
        # Generate HMAC of received data and compare to transmitted HMAC
        key = hashlib.sha256(aes_key).digest()  # Hash the AES key
        h = hashlib.sha256()  # Create an SHA256 hash object
        h.update(ciphertext)  # Update the hash object with the ciphertext
        h.update(tag)  # Update the hash object with the tag
        
        # Compare the computed HMAC with the transmitted HMAC
        if not h.digest() == mac:
            print("Data corrupted! HMAC does not match.")
            sys.exit(1)
        
        # Decrypt message with AES key
        cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce)  # Create an AES cipher object
        plaintext = cipher_aes.decrypt_and_verify(ciphertext, tag)  # Decrypt the ciphertext using the AES key and verify the tag
        
        os.chdir(subdir_path_receiver)
        
        # Write decrypted message to received_message.txt
        with open('received_message.txt', 'wb') as f:
            f.write(plaintext)
        
        # Indicate successful execution of program
        print("Message received and saved to location cs4600_FinalProj\\Receiver\\received_message.txt!")
        sys.exit(0)
    except SystemExit:
        pass  # Ignore the SystemExit exception and continue executing
    except:
        # Indicate potential data curroption/tampering and exit program wiht failure status
        print("Warning Data Has Been Currupted!")
        sys.exit(1)

else:
    # Indicate Failed execution of program
    print("Error No Directory {subdir_path_receiver_keys}")
