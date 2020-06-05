class b1 :
    n = 0

    def setdata(self,x) :
        self.n = x


class c1(b1) :
    def display(self) :
        a = 1
        i = 0
        while(i <= self.n) :
            a = a + i
            print(a)
            i = i + 1

