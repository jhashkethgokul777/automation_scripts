#Lists all files in a folder

import os

source = r"C:\Users\jhask\OneDrive\Documents"
files = os.listdir(source)

for f in files:
    print(f)

print("\n Task Completed!")