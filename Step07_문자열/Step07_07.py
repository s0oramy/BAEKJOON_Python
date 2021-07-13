a, b = map(int, input().split())

changeA = list(str(a))
changeA.reverse()
newA = ''
for a in changeA :
    newA += str(a)

changeB = list(str(b))
changeB.reverse()
newB = ''
for b in changeB :
    newB += str(b)

print(max(newA, newB))