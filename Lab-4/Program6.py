row=int(input("number="))
for i in range(1,row+1):
    print(" "*(row-i) + " ".join(chr(65 + j) for j in range(i)))
