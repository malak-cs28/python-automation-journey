#Task 1
import os

folder="new folder"
if os.path.exists(folder):
    os.chdir(folder)
else:
    os.mkdir(folder)
    os.chdir(folder)
    
paths=[]

for n in range (1,4):
    paths.append(os.path.join(folder,f"file{n}.txt"))
    with open(f'file{n}.txt',"w") as file:
        file.write(f"this is file number {n}")
        n+=1
        
        
files=os.listdir()
print(files)