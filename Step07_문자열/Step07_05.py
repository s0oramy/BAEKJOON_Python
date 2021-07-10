word = input().lower()
word_list = list(set(word))
new = []

for i in word_list :
    count = word.count(i)
    new.append(count)

if new.count(max(new)) >= 2 :
    print('?')
else :
    print(word_list[(new.index(max(new)))].upper())