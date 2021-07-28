m = int(input())
n = int(input())
list = []
for a in range(m, n+1):
    count = 0
    if a > 1:
        for i in range(2, a):
            if a % i == 0:
                count += 1
                break
        else:
            list.append(a)
                
if sum(list) == 0:
    print (-1)
else:
    print(sum(list))
    print(min(list))