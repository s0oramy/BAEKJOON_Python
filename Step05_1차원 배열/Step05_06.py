t = int(input())
for i in range(t):
    count = 0
    sum = 0
    a = list(input())
    for i in a:
        if i == 'O':
            count += 1
            sum = sum + count 
        else:
            count = 0
    print(sum)