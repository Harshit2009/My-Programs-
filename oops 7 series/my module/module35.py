class b1 :
    a =0

    def setdata(self,x) :
        self.a = x


class c1(b1) :
    def display(self) :
        r = 0
        s = 0
        t = self.a
        while(t != 0) :
            r = t%10
            s = s+r*r*r
            t = int(t/10)
        print(s)
        if(s == self.a) :
            print("Given number is an armstrong number")
        else :
            print("Given number is not an armstrong number")
            
