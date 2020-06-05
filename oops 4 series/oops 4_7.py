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

class Developer(Employee) :
    raise_amt = 1.10

    def __init__(self,first,last,pay,prog_lang) :
        super().__init__(first,last,pay)
        Employee.__init__(self,first,last,pay)


dev_1 = Employee('Harshit', 'Goel', 50000)
dev_2 = Employee('Ajay', 'Sharma', 60000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
        
