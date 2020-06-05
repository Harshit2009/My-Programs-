class b1 :
    radius = 0
    
    def setdata(self,x) :
        self.radius = x

class c1(b1) :        
    area = 0
    def area(self) :
        self.area = self.radius * self.radius * 3.14

    def display(self) :
        print("The area of circle is :"+str(self.area))

c =c1()
c.setdata(20)
c.area()
c.display()
        
