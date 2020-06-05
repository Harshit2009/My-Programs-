class SectionA :
    a =0

    def setdata(self,x) :
        self.a = x

    def display(self) :
        for i in range(self.a,1,-1) :
            print()
            for j in range(i,1,-1) :
                print("*",end=' ')

c = SectionA()
c.setdata(6)
c.display()
