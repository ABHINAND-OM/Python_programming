def pal(n):
    s=0
    temp=n
    while(n>0):
        r=n%10
        s=s*10+r
        n=n//10
    print(s)
    if(temp==s):
        print("the number is palindrome")
    else:
        print("the number is not palindrome")
n=int(input("enter a number:"))
pal(n)
