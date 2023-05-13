# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:23:31 2023

@author: khale

"""
import sys
from Crypto.PublicKey import RSA

# Generate a 2048-bit RSA key pair for the sender
sender_key = RSA.generate(2048)
with open("sender_private_key.pem", "wb") as f:
    f.write(sender_key.export_key())
with open("sender_public_key.pem", "wb") as f:
    f.write(sender_key.publickey().export_key())

# Generate a 2048-bit RSA key pair for the receiver
receiver_key = RSA.generate(2048)
with open("receiver_private_key.pem", "wb") as f:
    f.write(receiver_key.export_key())
with open("receiver_public_key.pem", "wb") as f:
    f.write(receiver_key.publickey().export_key())


print("RSA Keys Generated!!!")
sys.exit(0)