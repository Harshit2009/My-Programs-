def fact(z) :
    f=int(1)
    i=1;
    for i in range(1,z+1) :
        f=f*i
    return(int(f))
n=int(input("Enter value of n\t\t"))
r=int(input("Enter value of r\t\t"))
f1=fact(n)
print(f1)
f2=fact(r)
print(f2)
f3=fact(n-r)
print(f3)
res=int(f2*f3)
print(res)
res1=int(f1/res)
print(res1)



