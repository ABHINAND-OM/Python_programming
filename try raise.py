try:
    num=int(input("enter a positive integer"))
    if(num<=0):
        raise ValueError("this is a negative number")
except ValueError as e:
    print(e)