n = int(input())
count = n
for i in range(n):
    word = input()
    for w in range(len(word)-1):
        if word.find(word[w]) > word.find(word[w+1]):
            count = count - 1
            break
print(count)