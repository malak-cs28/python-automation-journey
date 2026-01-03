import os 
folder = "files"  # Name of the folder you want to check

files = os.listdir(folder)  # Get list of contents

print(files)  # Print the list
old_path=os.path.join(folder,"file1.txt")
new_path=os.path.join(folder,"first_file.txt")

os.rename(old_path,new_path)


print(files)