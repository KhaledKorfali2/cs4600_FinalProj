# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:23:31 2023

@author: khale

"""
import os
import sys
from Crypto.PublicKey import RSA


# Generate a 2048-bit RSA key pair for the sender
sender_key = RSA.generate(2048)

# Generate a 2048-bit RSA key pair for the receiver
receiver_key = RSA.generate(2048)

#Define the name of the main director folder
main_dir = os.getcwd()

# Define the name of the subdirectory to read
sender_dir = "Sender"
sender_keys_dir = "Sender_Keys"

# Get the full path of the subdirectory
subdir_path_sender = os.path.join(os.getcwd(), sender_dir)

# Get the full path of the subdirectory
subdir_path_sender_keys = os.path.join(subdir_path_sender, sender_keys_dir)


# Check if the subdirectory does not exist
if not os.path.isdir(subdir_path_sender):
    os.mkdir(subdir_path_sender)
os.chdir(subdir_path_sender)

with open("message.txt", "w") as f:
    f.write("Enter Message Here")

if not os.path.isdir(subdir_path_sender_keys):
    os.mkdir(subdir_path_sender_keys)
os.chdir(subdir_path_sender_keys)
    
with open("sender_private_key.pem", "wb") as f:
    f.write(sender_key.export_key())
with open("sender_public_key.pem", "wb") as f:
    f.write(sender_key.publickey().export_key())
with open("receiver_public_key.pem", "wb") as f:
    f.write(receiver_key.publickey().export_key())

#Go back to main directory folder
os.chdir(main_dir)


# Define the name of the subdirectory to read
receiver_dir = "Receiver"
receiver_keys_dir = "Receiver_Keys"

# Get the full path of the subdirectory
subdir_path_receiver = os.path.join(os.getcwd(), receiver_dir)

# Get the full path of the subdirectory
subdir_path_receiver_keys = os.path.join(subdir_path_receiver, receiver_keys_dir)



# Check if the subdirectory does not exist
if not os.path.isdir(subdir_path_receiver):
    os.mkdir(subdir_path_receiver)
os.chdir(subdir_path_receiver)

if not os.path.isdir(subdir_path_receiver_keys):
    os.mkdir(subdir_path_receiver_keys)
os.chdir(subdir_path_receiver_keys)
    
with open("receiver_private_key.pem", "wb") as f:
    f.write(receiver_key.export_key())
with open("receiver_public_key.pem", "wb") as f:
    f.write(receiver_key.publickey().export_key())
with open("sender_public_key.pem", "wb") as f:
    f.write(sender_key.publickey().export_key())

print("RSA Keys Generated!!!")
sys.exit(0)