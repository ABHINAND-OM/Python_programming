f=input("enter a file name:")
try:
    f1=open(f,"r")
except:
    print("no file named",f)