class Student :

    def __init__(self,name,rollno,marks) :
        self.name = name
        self.rollno = rollno
        self.marks = marks

sub_1 = Student('Harshit Goel',18078,25)
sub_2 = Student('Harshit Goel',18078,50)
sub_3 = Student('Harshit Goel',18078,75)
sub_4 = Student('Harshit Goel',18078,100)

print(sub_1.name,sub_1.rollno,sub_1.marks)
print(sub_2.name,sub_2.rollno,sub_2.marks)
print(sub_3.name,sub_3.rollno,sub_3.marks)
print(sub_4.name,sub_4.rollno,sub_4.marks)
