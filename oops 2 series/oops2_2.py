class Employee :

    def __init__(self,first,last,pay) :
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@compnay.com'
    
    def fullname(self) :
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self) :
        self.pay = int(self.pay * 1.04)
    

emp_1 = Employee('Harshit','Goel',60000)
emp_2 = Employee('Ajay','Sharma',50000)

print("Salary of Employee 1 before raise is :"+str(emp_1.pay))
emp_1.apply_raise()
print("Salary of Employee 1 after raise is :"+str(emp_1.pay))

print("Salary of Employee 2 before raise is :"+str(emp_2.pay))
emp_2.apply_raise()
print("Salary of Employee 2 after raise is :"+str(emp_2.pay))
