class SectionA :
    a=0
    b=0
    sum=0

    def setdata(self,x,y):
        self.a = x
        self.b = y

    def sum(self):
        self.sum = self.a + self.b

    def display(self) :


        print(self.sum)
        

c = SectionA()
c.setdata(2,4)
c.sum()
c.display()
