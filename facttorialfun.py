def fact(a):
    if(a==1):
        return a
    else:
        return a*fact(a-1)
    if a==0:
        print("factorial does not exit")
        