list = []
cycle = 0
while cycle < 10:
    x = int(input())
    result = x % 42
    list.append(result)
    cycle = cycle + 1

box = []
for i in range(10):
    if list[i] not in box:
        box.append(list[i])
print(len(box))