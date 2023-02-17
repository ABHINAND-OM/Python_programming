student={}
n=int(input("enter the number of students:"))
for i in range(0,n):
    a=input("enter the names of the student:")
    student[a]=int(input("enter the mark of the student"))
print(student)
b=[]
b+=student.keys()
b.sort()
for i in b:
    print(i,":",student[i])