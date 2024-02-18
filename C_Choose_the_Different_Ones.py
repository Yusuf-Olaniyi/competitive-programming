num_test =  int(input())

while num_test > 0:
    n,m,k = map(int,input().split())
    a = sorted(set(map(int,input().split())))
    b = sorted(set(map(int,input().split())))
    #print(a)
    #print(b)
    count_a = 0
    count_b = 0
    common = 0
    for i in range(1,k+1):
        if i in a and i in b:
            common += 1
        elif i in a:
            count_a +=1 
        elif i in b:
            count_b += 1
    #print(f'count_a before common {count_a}')
    #print(f'count_b before common {count_b}')
    #print(f'common {common}')
    if common % 2 == 0:
        count_a += int(common/2)
        count_b += int(common/2)
    else:
        if count_a < count_b:
            count_a += common
        else:
            count_b += common
    #print(f'count_a {count_a}')
    #print(f'count_b {count_b}')
    if count_a == k/2 and count_b == k/2:
        print('YES')
    else:
        print('NO')
    num_test -= 1