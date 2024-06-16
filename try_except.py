
try:
    num2 = 10/0
    num1 = int(input("Enter the number: "))
    print(num1)
except ValueError as e:
    print(e)
except ZeroDivisionError as z:
    print(z)