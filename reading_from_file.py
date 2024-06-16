
employees_file = open("employee.txt", "r")

for emp in employees_file.readlines():
    print(emp)

employees_file.close()