class b1 :
    a =0

    def setdata(self,x) :
        self.a = x


class c1(b1) :
    def display(self) :
        for i in range(self.a,1,-1) :
            print()
            for j in range(i,1,-1) :
                print("*",end=' ')

c = c1()
c.setdata(6)
c.display()
