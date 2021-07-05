list = []
count = 0
while count != 9 :
    num = int(input())
    count = count + 1
    list.append(num)
print(max(list))
print(list.index(max(list))+1)
