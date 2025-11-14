#Replacing underscores with spaces 
#you can also reverse it

import os

folder = r"C:\Users\jhask\OneDrive\Documents\auto_testing"

for filename in os.listdir(folder):
    new_name = filename.replace(" ", "_")
    os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
    print(f"{filename} -> {new_name}")