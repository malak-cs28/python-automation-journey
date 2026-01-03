import os 
folder = "files"  # Name of the folder you want to check

files = os.listdir(folder)  # Get list of contents

print(files)  # Print the list
old_path=os.path.join(folder,"file1.txt")
new_path=os.path.join(folder,"first_file.txt")

# os.rename(old_path,new_path)


print(files)


# os.remove(os.path.join(folder,"file2.txt"))

# print(files)

#file i know exists
print(os.path.exists(new_path))

#file i know dont exist 
print(os.path.exists(old_path))



os.remove(new_path)

os.rmdir(folder)#deletes empty files only 

print(files)