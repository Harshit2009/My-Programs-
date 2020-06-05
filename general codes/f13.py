def fseries5(t1,t2,n) :
    for i in range(1,n,+1) :
        print(t1)
        term=t1+t2
        t1=t2
        t2=term
fseries5(0,1,10)        
