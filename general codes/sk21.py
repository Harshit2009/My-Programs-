class SectionA :
    a = 0
    
    def setdata(self,x) :
        self.a = x

    def display(self) :
        j = 0
        for i in range(2,self.a,+1) :
            if(self.a%i == 0) :
                j=1
        if(self.a == 1) :
            print("1 is neither prime nor composite")
        else :
            if(j == 0) :
                print("number is a prime")
            else :
                print("number is not a prime")

c =SectionA()
c.setdata(37)
c.display()
        
