#enter an integer of your choice
n=int(input("Enter a number:"))
t=n
rev=0
#reverse number
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
#print output
print("Reverse of the number",t,"is",rev)
