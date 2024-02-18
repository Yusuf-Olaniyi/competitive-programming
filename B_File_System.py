n = int(input())
files = dict()
i = 1
while n > 0:
    file = ''.join(list(map(str,input().split())))
    if file in files:
        print(f'{file}{files[file]}')
        files[file] += 1
        
    else:
        files[file] = 1
        print('OK')


    n-=1 

