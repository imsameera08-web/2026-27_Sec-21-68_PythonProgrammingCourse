# Count frequency of each word in a sentence

sentence = input("Enter a sentence: ")
words = sentence.split()

count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print(count)