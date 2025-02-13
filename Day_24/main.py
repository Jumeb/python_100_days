with open("my_file.txt", mode="a") as file:
    contents = file.read()
    print(contents)
    file.write("\nJames")
    contents = file.read()
    print(contents)