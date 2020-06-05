class SectionA :
    a = 0
    
    def setdata(self,x) :
        self.a = x

    def display(self) :
        if(self.a % 2 == 0) :
            print("Number is divisible by 2")
        else :
            print("Number is not divisible by 2")

c =SectionA()
c.setdata(20)
c.display()
        
