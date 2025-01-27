#enter integer
n=int(input("Enter an integer:"))
for i in range(1, n+1):
    if n%i==0:
    #print output
        print(i, end="\n")
