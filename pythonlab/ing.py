n=input("enter a string")
if n[-3:]=='ing':
    n=n+'ly'
else:
    n=n+'ing'
print(n)