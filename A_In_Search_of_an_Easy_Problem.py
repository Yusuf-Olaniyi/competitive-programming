n_test = int(input())

opinion = sorted(map(int,input().split()))

if opinion[-1] == 1:
    print('HARD')
else:
    print('EASY')