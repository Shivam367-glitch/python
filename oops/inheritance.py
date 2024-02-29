class A:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def printDetails(self):
        print("parent")


# Inheritance
class B(A):
    pass


class Student(A):
    def __init__(self, name, age, phone, roll_number):
        super().__init__(name, age, phone)
        self.roll_number = roll_number

    def printDetails(self):
        super().printDetails()
        return f"Name: {self.name}, Age: {self.age}, Phone: {self.phone}, Roll Number: {self.roll_number}"


# obj_B = B("ab", 25, 8820239869)
# print(obj_B.name)  # Accessing inherited attribute
# print(obj_B.age)  # Accessing inherited attribute
# print(obj_B.printDetails())  # Accessing inherited method

obj_Student = Student("John", 20, 1234567890, "A1234")
print(obj_Student.name)  # Accessing inherited attribute
print(obj_Student.age)  # Accessing inherited attribute
print(obj_Student.phone)  # Accessing inherited attribute
print(obj_Student.roll_number)  # Accessing additional attribute in Student class
print(obj_Student.printDetails())  # Accessing overridden method in Student class
