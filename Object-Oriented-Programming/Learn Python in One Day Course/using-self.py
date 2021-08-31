class ProgStaff:
    companyName = 'ProgrammingLab'
    
    def __init__(self, pSalary):
        self.salary = pSalary
    
    def printInfo(self):
        print("Company name is ", ProgStaff.companyName)
        print("Salary is ", self.salary)

peter = ProgStaff(2500)
john = ProgStaff(1500)

print(peter.companyName)
print(john.companyName)
print(peter.salary)
print(john.salary)

ProgStaff.companyName = 'ProgrammingSchool' # This overwrites the global class variable with ProgrammingSchool, this applies to both peter and john

print(peter.companyName)
print(john.companyName)

peter.salary = 2700 #This only effects Peter and not John
print(peter.salary)
print(john.salary)