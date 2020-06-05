t1=0
t2=1
n=int(input("Enter the of terms"))
print("Fibonacci Series:")
for i in range(1,n,+1) :
    print(t1)
    term=t1+t2
    t1=t2
    t2=term
