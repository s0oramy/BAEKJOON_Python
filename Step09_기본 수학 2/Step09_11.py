import math

t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1- x2) ** 2 + (y1 -y2) ** 2)

    a = r1 + r2
    b = abs(r1 - r2)
    
    if b > d or d > a:
        print(0)
    elif (d == a or d == b) and d != 0:
        print(1)
    elif b < d < a:
        print(2)
    else:
        print(-1)