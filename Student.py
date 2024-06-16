class Student:
    def __init__(self,name,age,year,faculty):
        self.name = name
        self.age = age
        self.year = year
        self.faculty = faculty
    def on_honour_roll(self):
        print("The name of student is "+ self.name)


obj1 = Student("Chiranjivi Baskota", 20, "4th year", "BCT")

print(obj1.name)
print(obj1.age)
print(obj1.year)
print(obj1.faculty)

obj1.on_honour_roll()
