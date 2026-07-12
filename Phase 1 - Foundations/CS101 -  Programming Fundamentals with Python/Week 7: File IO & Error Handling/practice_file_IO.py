with open('data.txt', 'r') as file:
    for f in file:
        print(f)

with open('sample.txt', 'w') as file:
    file.write("This is the first line.\n")
    file.write("Is the file overwritten by this?")

with open('sample.txt', 'r') as file:
    contents = file.read()
    print(contents)

with open('sample.txt', 'w') as file:
    file.write("This is the first line.\n")

with open('sample.txt', 'r') as file:
    contents = file.read()
    print(contents)