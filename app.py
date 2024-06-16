
def max_num(num1,num2,num3):
    maxi = num1
    if num2>=maxi:
        maxi = num2
    if num3>=maxi:
        maxi = num3

    return maxi

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

print("The maximum number is "+ str(max_num(int(num1),int(num2),int(num3))))








