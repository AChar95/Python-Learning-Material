class Staff:
    #This initiates the class object
    def __init__(self, pPosition, pName, pPay):
        self._position = pPosition # This _position is to indicate to other programmers that position should not be accessed directly
        self.name = pName
        self.pay = pPay
        print("Creating Staff object")
    
    def __str__(self):
        return "Position = %s, Name = %s, Pay = %d" %(self._position, self.name, self.pay)
    
    def calculatePay(self):
        prompt = "\nEnter number of hours for %s " %(self.name)
        hours = input(prompt)
        prompt = "\nEnter the hourly rate for %s " %(self.name)
        hourlyRate = input(prompt)
        self.pay = int(hours)*int(hourlyRate)
        return self.pay
    
    @property
    def position(self):
        print("Getter method")
        return self._position
    @position.setter
    def position(self, value):
        if value == 'Manager' or value == 'Basic':
            self._position = value
        else:
            print("Position is invalid, no changes have been made")

officeStaff1 = Staff('Basic','Yvonne', 0)

officeStaff1.name
officeStaff1.calculatePay()
print(officeStaff1)

officeStaff1.position

officeStaff1.position = 'Manager'
print(officeStaff1.position)