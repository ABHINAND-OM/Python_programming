def sumn(num):
    sum=0
    for i in range(1,num+1):
        sum=sum+i
    return sum
num=int(input("enter a number:"))
print("the sum of till",num,"is",sumn(num))
