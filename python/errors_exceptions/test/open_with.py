#!/usr/bin/python3
try:
    with open("mydata2.txt") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found. Please provide the correct file name or path.")
except IOError as e:
    print("An error occurred while reading the file:", e)
except Exception as r:
    print("An error occurred:", r)
else:
    print("File content:")
    print(content)
