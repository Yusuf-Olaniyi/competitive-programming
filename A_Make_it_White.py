n_test = int(input())

while n_test:
    lenght = int(input())
    word = input()
    paint = []
    for i in range(lenght):
        if word[i] == 'B':
            paint.append(i)

    print(max(paint) - min(paint) + 1)

    n_test -= 1