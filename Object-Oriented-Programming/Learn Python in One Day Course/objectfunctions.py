class ParentClass:
    def __init__(self):
        self.a = 1
        print("Parent Class Object Created")
    def someMethod(self):
        print('Hello')

class ChildClass(ParentClass):
    def __init__(self):
        print("Child Class Objet Created")
        
parent = ParentClass()
child = ChildClass()

try:
    isinstance(parent, MyClass)     #This checks to isinstance(A,B) is A an instance (class or subclass) of B. Will resolve with a boolean. If B is tuple e.g. (B, C), as long as A is an instance of B or C then it will respond true
except NameError:
    print("No such class")
    
print(issubclass(ChildClass, ParentClass))         # true
print(issubclass(ParentClass, ParentClass))        # true
print(issubclass(ChildClass, int))                 # false
print(issubclass(ChildClass, (ParentClass, int)))  # true