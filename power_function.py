
def raise_to_power(base_num, pow_num) :
    result=1
    for index in range(pow_num) :
        result = result * base_num

    return result

base_num = int(input("Enter the base number: "))
pow_num = int(input("Enter the power number: "))

print(raise_to_power(base_num,pow_num))
