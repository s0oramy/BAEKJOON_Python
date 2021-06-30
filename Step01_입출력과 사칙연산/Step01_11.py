a = int(input())
b = int(input())
third = a * (b % 10)
fourth = a * (b % 100 // 10)
fifth = a * (b // 100)
sixth = a * b

print(third)
print(fourth)
print(fifth)
print(sixth)