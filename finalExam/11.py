class Employee:
    def __init__(self,first, last):
        self.firstname = first
        self.lastname = last
        self.fullname = f'{self.firstname} {self.lastname}'
        self.email = f'{self.firstname.lower()}.{self.lastname.lower()}@company.com'


emp_1 = Employee("John","Smith")
print(emp_1.fullname)
print(emp_1.email)
print(emp_1.email)
#教你如何使用这个框架

