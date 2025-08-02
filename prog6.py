text="apple,banana,apple,orange,banana,orange,apple"
word_counts={}
for word in text.split():
    if word in word_counts:
        word_counts[word] +=1
    else:
        word_counts[word]=1
for word ,count in word_counts.items():
        print(f"{word}:{count}")

