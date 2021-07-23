#5의 배수가 아니라 3의 배수를 먼저 생각해볼 것
n = int(input())
count = 0
while n >= 0:
    if n % 5 == 0:
        count += n // 5
        print(count)
        break
    n -= 3       # 위치 중요(앞으로 가면 원래 5의 배수인 것도 변질됨)
    count += 1
else:
    print(-1)