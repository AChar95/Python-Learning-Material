class A:
    
    def __init__(self):
        self.__x = 5
        self._y = 6


varA = A()
print(varA._y) # This prints out 6
print(varA.__x) ## This gives an error as x is hidden, the python compiler recognises this as _A__x
