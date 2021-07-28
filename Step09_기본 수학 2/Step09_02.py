m = int(input())
n = int(input())
list = []
for _ in range(m, n+1):
    count = 0
    if _ > 1:
        for i in range(2, _):
            if _ % i != 0:
                count += 1
            if count == _ - 2:
                list.append(_)
                
if sum(list) == 0:
    print (-1)
else:
    print(sum(list))
    print(min(list))