n = int(input())
total = 0
for i in range(1, n + 1):
    sum = total + i
    total = sum
print(total)