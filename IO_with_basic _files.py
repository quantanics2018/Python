# Using double backslashes
with open("F:\\New folder (2)\\1.txt", "r") as file:
    content = file.read()

with open("F:\\New folder (2)\\2.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a new line.")

with open("F:\\New folder (2)\\3.txt", "a") as file:
    file.write("\nThis is an appended line.")

try:
    with open("F:\\New folder (2)\\4.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
