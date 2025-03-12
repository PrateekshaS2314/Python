print("(line by line)")
with open("textfile.txt", "r") as f:
    print("Line1: ", f.readline(), end = " ")
    print("Line2: ", f.readline(), end = " ")
print("")
