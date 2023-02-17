try:
    a=int(input("enter a"))
    b=int(input("enter b"))
    c=a/b
    print(c)
except Exception:
    print("cant divided by zero")
    print(Exception)
else:
    print("hi iam also else block")