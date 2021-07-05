a = int(input())
b = int(input())
c = int(input())
result = a * b * c
change = str(result)

for i in range(10):
    print(change.count(str(i)))
