croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for i in croatia :
    word = word.replace(i, '*')  
print(len(word))

'''
word = input()
count = 0
for w in range(len(word)) : 
    if word[w] == '=' or word[w] == '-': count += 0
    elif word[w] == 'z' or word[w] == 'j' :
        if word[w-1] == 'd' or word[w-1] == 'n' or word[w-1] == 'l': count += 0
        else: count += 1
    else : count += 1
print(count)
'''