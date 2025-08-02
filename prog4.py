student={}
for i in range(3):
    print(f"\n enter the student details{i+1}:")
    rollno=int(input("enter the roll no:"))
    name=input("enter the name :")
    student[rollno]=name
    print("\n student dictionary")
    print(student)    