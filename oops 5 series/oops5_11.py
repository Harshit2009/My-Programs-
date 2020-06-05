class Employee :
    raise_amt = 1.04

    def __init__(self,first,last,pay) :
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        
    def fullname(self) :
        return '{} {}'. format(self.first, self.last)

    def apply_raise(self) :
        self.pay = int(self.pay * self.raise_amt) 

    def __repr__(self) :
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self) :
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other) :
        return self.pay + other.pay
    
emp_1 = Employee('Harshit', 'Goel', 50000)
emp_2 = Employee('Ajay', 'Sharma', 60000)

print(len('test'))
print('test'.__len__())

        
