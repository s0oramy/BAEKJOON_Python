num = list(map(int, input().split()))
list = []
for a in range(num[0], num[1]+1):
    if a > 1:
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                break
        else:
            list.append(a)

for l in list:
    print(l)