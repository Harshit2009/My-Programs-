#error due to call without self by object

class Employee :
    
    def __init__(self,first,last,pay) :
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname() :
        return '{} {}'.format(self.first,self.last)
     
emp_1 = Employee('Harshit','Goel',50000)
emp_2 = Employee('Ajay','Sharma',60000)

print(emp_2.fullname())
