n = int(input())

if n < 10 :
    first_cycle = 0 + n
    newNum = newNum = (first_cycle * 10) + first_cycle
    cycle = 1
else :
    first_cycle = (n // 10) + (n % 10)
    newNum = ((n % 10)* 10) + (first_cycle % 10)
    cycle = 1

while n != newNum :
    way = (newNum // 10) + (newNum % 10)
    newNum = ((newNum % 10)* 10) + (way % 10)
    cycle = cycle + 1
print(cycle)