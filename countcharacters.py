string=input("enter a string:")
count=0
for i in range(0,len(string)):
    if (string[i]!=' '):
        count=count+1
print("total no.of characters in the string",count)