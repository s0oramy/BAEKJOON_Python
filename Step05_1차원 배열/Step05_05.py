n = int(input())
scoreList = list(map(int, input().split()))
m = max(scoreList)

newList = []
for i in scoreList:
    newList.append(i/m*100)
print(sum(newList)/n)