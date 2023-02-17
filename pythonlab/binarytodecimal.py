def con(n):
    s=0
    i=0
    while(n>0):
        r=n%10
        s=s+r*(2**i)
        i=i+1
        n=n//10
    print(s)
h=int(input("enter a binary number:"))
print("the binary value is:")
con(h)
