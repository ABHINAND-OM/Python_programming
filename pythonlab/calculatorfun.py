def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x%y

print("select a operation")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulus")
choice=int(input("enter your choice  (1/2/3/4/5)"))
num1=int(input("enter your first number:"))
num2=int(input("enter your second number:"))
if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))



