class SectionA :
    n = 0

    def setdata(self,x) :
        self.n = x

    def display(self) :
        a = 1
        i = 0
        while(i <= self.n) :
            a = a + i
            print(a)
            i = i + 1

c = SectionA()
c.setdata(5)
c.display()
