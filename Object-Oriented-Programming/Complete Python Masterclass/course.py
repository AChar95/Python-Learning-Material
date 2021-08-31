class Course:
    def __init__(self, name):
        self.__name = name # here the name property is private
        self.students = [ ]
        
    def add_students(self, student):
        self.students.append(student)
        self.__write_student(student)
    
    def student_count(self):
        return len(self.students)
    
    def get_course_name(self):
        return self.__name
  
    def __write_student(self, student): # Private function that cannot be accessed through the instances of the class
        print("Hello " + student)
    
    
    ''' The below values hardcode the values into the class
    name = "Python"
    students = ["Patrick", "Joe", "Brent"]
    ''' 
    
    '''
    c1 = Course("Python")
    c2 = Course("HTML")
    
    del c1  #(this deletes the object c1 from memory )
    '''
    #pass