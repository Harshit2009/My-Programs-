class b1 :
    a =0

    def setdata(self,x) :
        self.a = x


class c1(b1) :
    def display(self) :
        t1 = 0
        t2 = 1
        for i in range(self.a,1,-1) :
            print(t1)
            term = t1 + t2
            t1 = t2
            t2 = term

