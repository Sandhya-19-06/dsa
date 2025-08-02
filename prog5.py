n=int(input("enter number of names enter"))
guest_list=[]
print("enter guest names:")
for i in range(n):
    name=input(f"enter{i+1}name:")
    guest_list.append(name)
unique_guest= set(guest_list)
print("\n unique guest name:")
for name in unique_guest:
    print(name)    