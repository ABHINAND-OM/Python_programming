n=int(input("enter the number of students :"))
studlist=[]
for i in range (0,n):
    stud={}
    stud['name']=input("enter student name:")
    stud['branch']=input("enter the branch")
    stud['roll']=int(input("enter the roll number:"))
    studlist.append(stud)
print("name branch rollnumber")
print()
for i in range(0,n):
    print(studlist[i])