class Employee :
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Harshit'
emp_1.last = 'Goel'
emp_1.email = 'harshit.goel@company.com'
emp_1.pay = 50000

emp_2.first = 'Ajay'
emp_2.last = 'Sharma'
emp_2.email = 'ajay.sharma@company.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)
