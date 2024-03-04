try:
       f = open("C:/Users/Shivam/Desktop/Python/File Handling/text1.txt","w")
       f.write("new file created using python....................")
       f.close()
except FileNotFoundError:
    print("file not found...")