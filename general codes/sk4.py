class SectionA :
    fahrenheit = 0
    celcius = 0

    def setdata(self,x) :
        self.fahrenheit = x

    def celcius(self) :
        self.celcius = (self.fahrenheit - 32)*5/9

    def display(self) :
        print("The temperature in celcius is :"+str(self.celcius))

c =SectionA()
c.setdata(97)
c.celcius()
c.display()
        
