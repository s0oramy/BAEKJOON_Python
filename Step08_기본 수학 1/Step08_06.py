apt = [[0 for i in range(15)] for j in range(15)]
for i in range(1, 15) :
    apt[0][i] = i

for floor in range(1, 15) :
    for ho in range(1, 15) :
            apt[floor][ho] = apt[floor - 1][ho] + apt[floor][ho - 1]

t = int(input())
for i in range(t) :
    x = int(input())
    y = int(input())
    print(apt[x][y])