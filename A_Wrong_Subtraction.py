number , n = map(int,input().split())

for _ in range(n):
    if number % 10 == 0:
        number = int(number/10)
    else:
        number -= 1
print(number)