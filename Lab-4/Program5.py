row=int(input("number="))
for i in range(1,row+1):
    print(" "*(row-i) + " ".join(str(num) for num in range(1,i+1)))
