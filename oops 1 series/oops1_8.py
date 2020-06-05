class Employee :
    
    def __init__(self,first,last,pay) :
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self) :
        return '{} {}'.format(self.first,self.last)
     
emp_1 = Employee('Harshit','Goel',50000)
emp_2 = Employee('Ajay','Sharma',60000)

emp_2.fullname()
print(Employee.fullname(emp_1))
