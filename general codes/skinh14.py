class b1 :
    a = 0
    
    def setdata(self,x) :
        self.a = x


class c1(b1) :
    def display(self) :
        for i in range(self.a,0,-1) :
            print(i)

c = c1()
c.setdata(10)
c.display()
        
