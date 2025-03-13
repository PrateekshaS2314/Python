try:
    num = int(input("Enter a number:"))
    result = 10/num
    print(result)
except ValueError:
    print("Error: Invalid input")
except ZeroDivisionError:
    print("Error: Division by zero")
