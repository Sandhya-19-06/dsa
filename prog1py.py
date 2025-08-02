list=[]
for i in range(5):
    n=int(input("enter the numbers"))
    list.append(n)

print(list[0])
print(list[-1])
for i in list:
    print(i,end='')
print("\n reversed list")
list.reverse()
for i in list:
    print(i,end='')    
