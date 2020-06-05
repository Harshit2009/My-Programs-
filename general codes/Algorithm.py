def Algorithm(x,y):
    while(y):
        x,y=y,x%y
    return x
a=60
b=48
print("The gcd of 60 and 48 is :",end="")
print(Algorithm(60,48))
