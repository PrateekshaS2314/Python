n = int(input("Enter number:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")  # Print numbers from 1 to i
    print()  # Move to the next line after each row
