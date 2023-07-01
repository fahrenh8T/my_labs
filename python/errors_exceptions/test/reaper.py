#!/usr/bin/python3
try:
    file = open("mydata2.txt", "r")
    try:
        content = file.read()
    finally:
        file.close()
except FileNotFoundError as r:
    print("File not found. Please provide the correct file name or path.")
    print(r.args)
except IOError as r:
    print("An error occurred while reading the file:", r)
except Exception as w:
    print("An error occurred:", w)
else:
    print("File content:")
    print(content)
finally:
    print("Done")
