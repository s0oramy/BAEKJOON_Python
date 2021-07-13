dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
time = 0
for unit in dial:
    for i in unit:
        for x in a:
            if i == x:
                time += dial.index(unit) + 3
print(time)