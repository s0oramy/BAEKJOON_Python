t = int(input())
for x in range(1, t + 1):
    a, b = map(int, input().split())
    print('Case #', x, ':', sep = '', end = ' ')
    print(a, '+', b, '=', a + b)