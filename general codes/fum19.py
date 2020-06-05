def fum19(n,reverse) :
    orignal=n
    while(orignal!=0) :
        remainder=orignal%10
        reverse=reverse*10+remainder
        orignal=int(orignal/10)
        print(reverse)
    if(n==reverse) :
        print("Number is Palindrome")
    else :
        print("Nuber is not a Plindrome")
    
