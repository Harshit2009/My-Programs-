class b1 :
    a = 0
    
    def setdata(self,x) :
        self.a = x

class c1(b1) :
    def display(self) :
        if(self.a % 2 == 0) :
            print("Number is divisible by 2")
        else :
            print("Number is not divisible by 2")

