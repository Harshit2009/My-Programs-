class Student :
    pass


stu_1 = Student()

print(stu_1)

stu_1.name = input('Enter the name :')
stu_1.rollno = int(input('Enter the roll number of student'))
stu_1.marks = int(input('Enter the total marks of student'))

print(stu_1.name)
print(stu_1.rollno)
print(stu_1.marks)
