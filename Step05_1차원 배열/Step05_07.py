c = int(input())
for i in range(c):
    stscore = list(map(int, input().split()))
    average = sum(stscore[1:])/stscore[0]
    count = 0
    for x in stscore[1:]:
        if x > average:
            count += 1
    rate = count / stscore[0] * 100
    print('%0.3f' % float(rate) + '%')