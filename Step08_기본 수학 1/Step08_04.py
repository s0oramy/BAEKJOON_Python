a, b, v = map(int, input().split())
day = int((v-a)/(a-b))+1
if (v-a)%(a-b) == 0:
    print(day)
else:
    print(day + 1)