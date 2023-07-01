#!/usr/bin/python3
try:
    with open("test.py") as file:
        code = file.read()
        compiled_code = compile(code, filename="test.py", mode="exec")
        exec(compiled_code)
except SyntaxError as e:
    print("SyntaxError occurred:", e)
    print("Please check the syntax of the file.")
except FileNotFoundError:
    print("File not found. Please provide the correct file name or path.")
except Exception as e:
    print("An error occurred:", e)
