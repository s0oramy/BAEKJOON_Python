t = int(input())
for i in range(t) :
    h, w, n = map(int, input().split())
    floor = n % h
    num = n//h + 1
    if n % h == 0 :  # h의 배수
        num = n//h
        floor = h
    result = '{}'.format(floor*100 + num)
    print(result)