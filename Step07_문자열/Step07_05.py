words = input().lower()
words_list = list(set(words))
new = []

for i in words_list :
    count = words.count(i)
    new.append(count)

if new.count(max(new)) >= 2 :
    print('?')
else :
    print(words_list[(new.index(max(new)))].upper())