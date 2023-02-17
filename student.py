dictt={}
num=int(input("number"))
for i in range(num):
    a=input("enter the name")
    b = input("enter the mark")
    dictt[a]=b
lis=[]
lis+=dictt.keys()
lis.sort()
for i in lis:
    print(i,":",dictt[i])