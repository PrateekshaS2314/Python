print("all lines in a list")
with open("textfile.txt", "r") as f:
    print(f.readlines())
    for line in f:
        print(line.split(" "))
print("")
