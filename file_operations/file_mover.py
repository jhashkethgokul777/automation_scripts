#File mover

import os, shutil

source = r"C:\Users\jhask\OneDrive\Documents"
destination = r"C:\Users\jhask\OneDrive\Documents\auto_testing"

if not os.path.exists(destination):
    os.mkdir(destination)
    


for file in os.listdir(source):
    if file.endswith('.txt'):
        shutil.move(os.path.join(source, file), os.path.join(destination, file))
        print(f"Moved: {file}")