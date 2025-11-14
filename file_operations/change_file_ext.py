#changing fie extensions

import os

folder = r"C:\Users\jhask\OneDrive\Documents\auto_testing"

for filename in os.listdir(folder):
    if filename.endswith('.md'):
        base = filename[:-4]
        new_name = base + ".txt"
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
        print(f"{filename} -> {new_name}")