a=[]
lim=int(input("enter the limit of the string:"))
for i in range (lim):
    b=input("enter the string")
    a.append(b)
count=0
for i in a:
    for k in range(len(i)):
        if i[k]=='a':
            count+=1
print(count)