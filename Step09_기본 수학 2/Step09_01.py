n = int(input())
num = map(int, input().split())
prime = 0
for _ in num:
    error = 0
    if _ > 1:
        for i in range(2, _):
            if _ % i == 0:
                error += 1
        
        if error == 0 :
            prime += 1
print(prime)