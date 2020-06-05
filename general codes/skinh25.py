class b1 :
    a =0

    def setdata(self,x) :
        self.a = x


class c1(b1) :
    def display(self) :
        for i in range(self.a,11,+1) :
            j=i*i
            print(j)

c = c1()
c.setdata(1)
c.display()
