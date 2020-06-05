def fpattern7(j,n) :
    for i in range(1,n,+1) :
        print()
        for s in range(1,n-i,+1) :
            print()
            while(j!=2*i-1) :
                print(i,end=' ')
                j=j+1
fpattern7(0,5)            
