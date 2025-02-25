#SECURE-DATA-HIDING-IN-IMAGES-USING-STEGANOGRAPHY

This is a simple implementation of image-based steganography, where messages are hidden within an image and set with a password which is retrieved using the same passowrd. The encryption and decryption processes involve modifying the pixel values of an image to store message bytes without loss in image quality.
Features

    Hide a message inside an image using pixel manipulation with no loss in image quality.
    Secure the message with a password.
    Extract the hidden message only with the correct password.
    Simple and lightweight implementation using Python and OpenCV.

Requirement

Install Python from the official website: Python.org Make sure to install the IDLE alongside the installation of python and set environment variable. The following dependencies are necessary to run the scripts, to install use the below command on your terminal:

pip install opencv-python

Guide to get Started
To Encrypt

In order to hide a message in an image use the below command on your terminal where the project files exist:

python Image-encryptor.py

Steps:

    After running the script, the script will require an image, it will ask for image.jpg.
    Enter the message you want to hide.
    Enter a password in order to secure the image or if you want it without password just give the enter key.
    The encrypted image is saved as encImage.png.
    The password is stored in Key.txt.

To Decrypt

In order to retrieve the hidden message from the encImage.png:

python Image-decryptor.py -i encImage.png -p Key.txt

Steps:

    The script takes the input for the input field -i the encypted image.
    Provide the correct password file in the -p field or enter the corret password after the script prompts to enter.
    If only correct password is entered the script will output the hidden message from the encImage.png. Else it fail with the output Wrong Password, Try again!.

File Desc

    encrypt.py - Script to hide a message into an image.
    decrypt.py - Script to extract the secret message hidden inside the provided encrypted image.
    encImage.png- Image with the hidden message.
    Key.txt - Textfile with the password, which was used to set security.
    Pic.jpg - Unencrypted image which will be used to encrypt with a message.

Example
Encryption:

Enter the message to be encrypted: This is my project
Enter the password to secure your image: easypassword
'encImage.png' is your encrypted image

Decryption:

Enter the password used during encryption: easypassword
'This is my project' was the encrypted message decrypted from 'encImage.png' `

Edge case

Since during the encryption in the image, the pixel values with message bytes gets replaced, the message length shouldn't be longer than the image size.
License

This project is open-source and available under the MIT license
Author
Fawaz Hussain R
