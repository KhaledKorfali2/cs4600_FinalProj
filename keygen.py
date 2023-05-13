# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:23:31 2023

@author: khale

"""
import os
import sys
from Crypto.PublicKey import RSA

# Define the name of the subdirectory to read
sender_dir = "Sender"
sender_keys_dir = "Sender_Keys"

# Get the full path of the subdirectory
subdir_path_sender = os.path.join(os.getcwd(), sender_dir)

# Get the full path of the subdirectory
subdir_path_sender_keys = os.path.join(subdir_path_sender, sender_keys_dir)

# Check if the subdirectory exists
if os.path.isdir(subdir_path_sender):
    # # If the subdirectory exists, print its contents
    # print(f"Contents of {subdir_path_sender}:")
    # for file_name in os.listdir(subdir_path_sender):
    #     print(file_name)
    # Check if the subdirectory exists
    os.chdir(subdir_path_sender)
    if os.path.isdir(subdir_path_sender_keys):
        os.chdir(subdir_path_sender_keys)
        # Generate a 2048-bit RSA key pair for the sender
        sender_key = RSA.generate(2048)
        with open("sender_private_key.pem", "wb") as f:
            f.write(sender_key.export_key())
        with open("sender_public_key.pem", "wb") as f:
            f.write(sender_key.publickey().export_key())
    else:
        # If the subdirectory does not exist, print an error message
        print(f"Error: {subdir_path_sender_keys} directory does not exist.")
else:
    # If the subdirectory does not exist, print an error message
    print(f"Error: {subdir_path_sender} directory does not exist.")

os.chdir("..")
os.chdir("..")

# Define the name of the subdirectory to read
receiver_dir = "Receiver"
receiver_keys_dir = "Receiver_Keys"

# Get the full path of the subdirectory
subdir_path_receiver = os.path.join(os.getcwd(), receiver_dir)

# Get the full path of the subdirectory
subdir_path_receiver_keys = os.path.join(subdir_path_receiver, receiver_keys_dir)

# Check if the subdirectory exists
if os.path.isdir(subdir_path_receiver):
    # # If the subdirectory exists, print its contents
    # print(f"Contents of {subdir_path_receiver}:")
    # for file_name in os.listdir(subdir_path_receiver):
    #     print(file_name)
    # Check if the subdirectory exists
    os.chdir(subdir_path_receiver)
    if os.path.isdir(subdir_path_receiver_keys):
        os.chdir(subdir_path_receiver_keys)
        # Generate a 2048-bit RSA key pair for the receiver
        receiver_key = RSA.generate(2048)
        with open("receiver_private_key.pem", "wb") as f:
            f.write(receiver_key.export_key())
        with open("receiver_public_key.pem", "wb") as f:
            f.write(receiver_key.publickey().export_key())
    else:
        # If the subdirectory does not exist, print an error message
        print(f"Error: {subdir_path_receiver_keys} directory does not exist.")
else:
    # If the subdirectory does not exist, print an error message
    print(f"Error: {subdir_path_receiver} directory does not exist.")



print("RSA Keys Generated!!!")
sys.exit(0)