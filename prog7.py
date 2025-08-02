students={}
for i in range(3):
    name=input("enter name of student {i+1}:") 
    marks=int(input("enter the marks of student {i+1}:"))
    students[name]=marks
topper=max(students,key=students.get) 
print("topper is",topper,"with marks",students[topper])   
