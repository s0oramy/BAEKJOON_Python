n = int(input())
list = []
while 1:
    if n == 1:
        break
    for i in range(2, n + 1):
        if n % i == 0:
            list.append(i)
            n = n // i
            break

for l in list:
    print(l)