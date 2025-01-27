x=float(input("enter marks:"))
if x>=90:
    print("Grade A")
elif x>=70 and x<=89:
    print("Grade B")
elif x>=50 and x<=69:
    print("Grade C")
elif x>=35 and x<=49:
    print("Grade D")
elif x<=34:
    print("fail")
else:
    print("enter proper marks")
