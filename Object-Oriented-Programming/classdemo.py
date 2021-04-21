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
'''
officeStaff1 = Staff('Basic','Yvonne', 0)

officeStaff1.name
officeStaff1.calculatePay()
print(officeStaff1)

officeStaff1.position

officeStaff1.position = 'Manager'
print(officeStaff1.position)
'''

class ManagementStaff(Staff):
    def __init__ (self, pName, pPay, pAllowance, pBonus):
        super().__init__('Manager', pName, pPay)
        self.allowance = pAllowance
        self.bonus = pBonus
        #Staff.__init__('Manager', pName, pPay) alternative to using super()
        
    def calculatePay(self):
        basicPay = super().calculatePay()
        self.pay = basicPay + self.allowance
        return self.pay
    
    def calculatePerfBonus(self):
        prompt = "Enter performance grade for %s: " %(self.name)
        grade = input(prompt)
        if (grade == 'A'):
            self.bonus = 1000
        else:
            self.bonus = 0
        return self.bonus

class BasicStaff(Staff):
    def __init__(self, pName, pPay):
        super().__init__('Basic', pName, pPay)