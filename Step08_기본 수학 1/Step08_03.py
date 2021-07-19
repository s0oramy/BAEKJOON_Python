# 규칙을 찾아보면, 짝수 그룹과 홀수 그룹일 때 나누어서 구해야 함 
n = int(input()) # 구해야 하는 n번 째 수 

num_group = 0   # 사선으로 묶은 그룹
max_num = 0     # 입력된 숫자(n)의 라인에서 가장 큰 숫자
while n > max_num:
    num_group += 1
    max_num += num_group

gap = max_num - n
if num_group % 2 == 0 :  # 짝수 그룹일 때 
    top = num_group - gap
    under = gap + 1
else:                    # 홀수 그룹일 때 
    top = gap + 1
    under = num_group - gap

result = '{}/{}'.format(top, under)
print(result)