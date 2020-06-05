class b1:
    a=0
    b=0


    def setdata(self,x,y):
        self.a = x
        self.b = y

    

class c1(b1):
    sum1=0
    def sum(self):
        self.sum1 = self.a + self.b
    def display(self) :
        print(self.sum1)
            

c = c1()
c.setdata(2,4)
c.sum()
c.display()

    
