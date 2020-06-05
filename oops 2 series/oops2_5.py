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
        self.pay = int(self.pay * self.raise_amount)
    

emp_1 = Employee('Harshit','Goel',50000)
emp_2 = Employee('Ajay','Sharma',60000)

print(emp_1.pay)
print(emp_2.pay)
