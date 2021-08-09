import math

def checkValue(num):     #소수 구하는 함수 (3 5 7 11 ...)
    if num == 1:  #1은 소수가 아니다.
        return True
    else :
        for i in range(2, int(math.sqrt(num))+1) :
            if num % i == 0:
                return False
        return True

#소수를 리스트에 저장
all_list = list(range(2,246912)) # 문제에서 주어진 범위
save_list=[]

for a in all_list : # 주어진 범위 안의 소수들을 찾아서 저장해놓는다.
    if checkValue(a):
        save_list.append(a)

#사용자 입력 및 결과 출력
while (1):
    n = int(input())
    count = 0
    if n == 0:
        break
    for s in save_list:
        if n < s <= n * 2:
            count += 1
    print(count)