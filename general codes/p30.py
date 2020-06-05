n=int(input("Enter any number"))
j=0
for i in range(2,n,+1) :
    if(n%i==0) :
        j=1
if(n==1) :
    print("1 is neither prime nor composite")
else :
    if(j==0) :
        print("n is a prime number")
    else :
        print("n is not a prime number")
