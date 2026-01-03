

with open("sample.txt","r") as file:
    content=file.read()
    words=content.split()
    lines=content.splitlines()
   
print(f"character count: {len(content.strip())}") 
print(f"word count: {len(words)}")
print(f"line count: {len(lines)}")