def calc(a):
    value = sum(map(int,str(a))) + a
    return value

allNums = [i for i in range(1, 10001)]
num = []
for i in allNums:
    num.append(calc(i))

for i in allNums:
    if i in num:
        continue
    else:
        print(i)