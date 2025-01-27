#enter an integer of your choice
n=int(input("Enter a number:"))
t=n
rev=0
#reverse number
while n!=0:
    print("value of n is ",n)
    r=n%10
    print("value of r is ",r)
    rev=rev*10+r
    print("value of rev is ",rev)
    n=n//10
    print("value of n is ",n)
#print output
print("Reverse of the number",t,"is",rev)
