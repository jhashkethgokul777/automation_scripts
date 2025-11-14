#Rename Files to a Numbering Format
import os

folder = r"C:\Users\jhask\OneDrive\Documents\auto_testing"

for i, filename in enumerate(os.listdir(folder), start=1):
    new_name = f"file_{i}"
    os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
    print(f"{filename} -> {new_name}")