class Employee :
    raise_amount = 1.04

    def __init__(self,first,last,pay) :
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@compnay.com'
    
    def fullname(self) :
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self) :
        self.pay = int(self.pay * raise_amount)
    

emp_1 = Employee('Harshit','Goel',60000)
emp_2 = Employee('Ajay','Sharma',50000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
