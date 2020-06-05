class Student :
    def __init__(self) :
        pass
    def __init__(self,first,last,rollno) :
        self.first = first
        self.last = last
        self.rollno = rollno

    def input(self) :
        self.first = 'Ajay'
        self.last = 'Sharma'
        self.rollno = 56

    def fullname(self) :
        return '{} {} {}'.format(self.first,self.last,self.rollno)

stu_1 = Student(input('Enter the first name :'),input('Enter the last name :'),int(input('Enter the roll number of student :')))
stu_2 = Student(input('Enter the first name :'),input('Enter the last name :'),int(input('Enter the roll number of student :')))
print(stu_1.fullname())




