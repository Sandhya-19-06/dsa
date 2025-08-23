text=input("enter a string:")
freq={}
for ch in text:
    freq[ch]=freq.get(ch,0)+1
print("character frequency",freq)    