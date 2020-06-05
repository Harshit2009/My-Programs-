class Employee :
    raise_amt = 1.04

    def __init__(self,first,last) :
        self.first = first
        self.last = last

    @property
    def email(self) :
        return '{}.{}.@email.com'. format(self.first, self.last)

    @property
    def fullname(self) :
        return '{} {}'. format(self.first, self.last)

    @fullname.setter
    def fullname(self, name) :
        first, last = name.split(' ')
        self.first = first
        self.last = last

emp_1 = Employee('Harshit', 'Goel')
emp_1.fullname = 'Hardik Pruthi'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

        
