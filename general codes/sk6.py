class SectionA :
    radius = 0
    area = 0

    def setdata(self,x) :
        self.radius = x

    def area(self) :
        self.area = self.radius * self.radius * 3.14

    def display(self) :
        print("The area of circle is :"+str(self.area))

c =SectionA()
c.setdata(20)
c.area()
c.display()
        
