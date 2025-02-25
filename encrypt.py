#!/usr/bin/env python
import cv2
import argparse
import os

# Set up command-line arguments
parser = argparse.ArgumentParser(description="Encrypt a secret message into an image")
parser.add_argument("-i", "--image", required=True, help="Path to input image (e.g., image.png)")
args = parser.parse_args()

# Load the image
img = cv2.imread(args.image)
if img is None:
    print("Error: Could not open image.")
    exit()

# Ask for the secret message and passcode
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Save the password and the message length in key.txt (so that decryption knows how many characters to extract)
with open("key.txt", "w") as key_file:
    key_file.write(password + "\n")
    key_file.write(str(len(msg)) + "\n")

# Create dictionaries to map characters to ASCII values (and vice versa)
char_to_ascii = {chr(i): i for i in range(256)}

# Initialize coordinates for embedding (we will use a simple diagonal embedding)
n = 0
m = 0
z = 0
rows, cols, channels = img.shape

# Check that the image is large enough along the diagonal to hide the message
if len(msg) > min(rows, cols):
    print("Error: The message is too long for the image's available diagonal pixels.")
    exit()

# Embed each character's ASCII code into the image pixels along the diagonal
for ch in msg:
    # Set the pixel value at position (n, m) on channel z to the ASCII value of the character
    img[n, m, z] = char_to_ascii[ch]
    n += 1
    m += 1
    z = (z + 1) % 3  # Cycle through the 3 color channels

# Save the encrypted image as encImage.png
cv2.imwrite("encImage.png", img)
print("Encrypted image saved as encImage.png")
# Optionally, you can open the image automatically (Windows only):
# os.system("start encImage.png")
