#!/usr/bin/python3
try:
    file = open("mydata2.txt", "r")
    try:
        content = file.read()
    finally:
        file.close()
except FileNotFoundError:
    print("File not found. Please provide the correct file name or path.")
except IOError as r:
    print("An error occurred while reading the file:", r)
except Exception as w:
    print("An error occurred:", w)
else:
    print("File content:")
    print(content)
