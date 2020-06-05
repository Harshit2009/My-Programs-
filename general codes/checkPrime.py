def checkPrime(n):
    for loop in range(2,n):
        if((n%loop)==0):
            return False
        return True
    