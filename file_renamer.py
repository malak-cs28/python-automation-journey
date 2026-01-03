import os

folder = input("Enter the folder containing the file to rename: ")

if not os.path.exists(folder):
    print("Folder does not exist!")
    exit()

file = input("Enter the current file name (with extension): ")
old_path = os.path.join(folder, file)

if not os.path.exists(old_path):
    print("File doesn't exist!")
    exit()

updated_file_name = input("Enter the new file name (with extension): ")
new_path = os.path.join(folder, updated_file_name)

os.rename(old_path, new_path)
print(f"File renamed from '{file}' to '{updated_file_name}' successfully.")
