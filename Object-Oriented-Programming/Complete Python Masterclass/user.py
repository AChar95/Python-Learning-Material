class User:
    def __init__(self, fname, sname):
        self.__fName = fname
        self.__sname = sname
    
    def get_full_name(self):
        return self.__fName  + ' ' + self.__sname
    
    def get_user_login(self, username):
        print("Access Granted")
    
    def user_work(self):
        print(self.__fName + " is working")

class SuperUser(User):
    def __init__(self, fname, sname):
        User.__init__(self, fname, sname)
    '''
    The derived class will override any function that is also present in the inherited class. The above method will also pass through the variables to the user class (inherited class)
    def __init__(self):
        pass
    '''
    def super_user_work(self):
        print("Preforming super work")