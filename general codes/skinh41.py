class a :
    radius = 0
    
    def setdata(self,x) :
        self.radius = x

class b(a) :        
    area = 0
    def area(self) :
        self.area = self.radius * self.radius * 3.14

class c(b) :
    def display(self) :
        print("The area of circle is :"+str(self.area))

x = c()
x.setdata(20)
x.area()
x.display()
        
