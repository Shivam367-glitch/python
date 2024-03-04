try:
    f = open("C:/Users/Shivam/Desktop/Python/File Handling/text.txt")
    print(f.read())
    # Do something with the file
except FileNotFoundError:
    print("File not found. Please check the file path.")