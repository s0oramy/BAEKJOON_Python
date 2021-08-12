# 직사각형은 네 각의 크기가 모두 직각이고 마주 보는 두 변의 길이가 같음
# x좌표로 이루어진 네 개의 수와 y좌표로 이루어진 네 개의 수에서 각각 두 개씩 같은 수를 구할 수 있음
all_x = []
all_y = []
for i in range(3):
    x, y = map(int, input().split())
    all_x.append(x)
    all_y.append(y)

for t in range(3):
    if all_x.count(all_x[t]) == 1:
        x = all_x[t]
    if all_y.count(all_y[t]) == 1:
        y = all_y[t]
print(x, y)
