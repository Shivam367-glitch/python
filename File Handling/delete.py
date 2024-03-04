
import os

try:
    if os.path.exists("C:/Users/Shivam/Desktop/Python/File Handling/text1.txt"):
        os.remove("demofile.txt")
except FileNotFoundError:
    print("File not found.........")
else :
    print("file not exist")
