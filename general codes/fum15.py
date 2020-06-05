def fum15(n) :
    r=0
    s=0
    t=n
    while(t!=0):
        r=t%10
        s=s+r*r*r
        t=int(t/10)
    print(s)
    if(s==n):
    
        print("Given number is an amstrong number")
    else :
    
        print("Given number is not an amstrong number")

    
