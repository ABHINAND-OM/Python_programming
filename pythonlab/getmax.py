def getmax(b):
    return max(b,key=len)
a=[]
li=int(input("the limit of the element :"))
for i in range(0,li):
    e=input("enter the elements:")
    a.append(e)
print("the longest word in the list is:",getmax(a))
