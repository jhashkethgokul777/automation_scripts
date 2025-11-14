#Check if a folder exists, if not - create it

import os

folder = r"C:\Users\jhask\OneDrive\Documents\auto_testing"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("folder created!")
else:
    print("Folder already exists!")
