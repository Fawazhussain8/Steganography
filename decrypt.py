#!/usr/bin/env python
import cv2
import argparse
import os

# Set up command-line arguments.
parser = argparse.ArgumentParser(
    description="Decrypt the hidden message from an encrypted image."
)
parser.add_argument(
    "-i", "--image", required=True,
    help="Path to the encrypted image (e.g., encImage.png)"
)
parser.add_argument(
    "-p", "--key",
    help="Path to the key file containing the passcode and message length (if omitted, you will be prompted)"
)
args = parser.parse_args()

# Load the encrypted image.
img = cv2.imread(args.image)
if img is None:
    print("Error: Could not open the encrypted image.")
    exit()

# If a key file is provided, read the stored passcode and message length.
if args.key:
    try:
        with open(args.key, "r") as key_file:
            stored_password = key_file.readline().strip()
            msg_length_str = key_file.readline().strip()
            if not msg_length_str.isdigit():
                print("Error: The message length in the key file is invalid.")
                exit()
            msg_length = int(msg_length_str)
    except FileNotFoundError:
        print("Error: Key file not found.")
        exit()
    # Do not prompt for a passcode; use the stored one.
    print("Using passcode from key file.")
    user_password = stored_password
else:
    # Prompt the user for the passcode (and message length) if no key file was provided.
    user_password = input("Enter passcode for Decryption: ")
    try:
        msg_length = int(input("Enter message length: "))
    except ValueError:
        print("Invalid message length.")
        exit()

# (In the provided encryption, no cryptographic operation is done using the passcode;
#  it’s simply stored for verification. If the key file was provided, we assume the password is correct.)

# Extract the hidden message from the image.
n = 0
m = 0
z = 0
rows, cols, channels = img.shape

if msg_length > min(rows, cols):
    print("Error: The stored message length exceeds the available diagonal pixels in the image.")
    exit()

# Map ASCII values back to characters.
ascii_to_char = {i: chr(i) for i in range(256)}
hidden_message = ""
for i in range(msg_length):
    ascii_val = img[n, m, z]
    hidden_message += ascii_to_char[ascii_val]
    n += 1
    m += 1
    z = (z + 1) % 3

print("Hidden message:", hidden_message)
