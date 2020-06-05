n = int(input("Enter an integer in decimal number"))
for c in range(31,0,-1) :
    k = n >> c
    if(k & 1) :
        print(1)
    else :
        print(0)
