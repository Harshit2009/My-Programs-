class SectionA :
    a =0

    def setdata(self,x) :
        self.a = x

    def display(self) :
        t1 = 0
        t2 = 1
        for i in range(self.a,1,-1) :
            print(t1)
            term = t1 + t2
            t1 = t2
            t2 = term

c = SectionA()
c.setdata(10)
c.display()
