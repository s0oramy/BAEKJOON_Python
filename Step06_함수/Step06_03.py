def calc(a):
    count = 0
    if a < 10 : count += 1
    elif a < 100 : count += 1
    else :
        blank = list(map(int, str(a)))
        if (blank[0] + blank[2])/2 == blank[1] :
            count += 1
        else: pass
    return count 

n = int(input())
final = 0
for i in range(1, n+1):
    final = final + calc(i)
print(final)