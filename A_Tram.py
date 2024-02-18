n_stop = int(input())

maximum = 0
p_existing = 0
for _ in range(n_stop):
    passengers = list(map(int,input().split()))
    p_enter = passengers[1]
    p_leaving = passengers[0]
    p_current = p_enter - p_leaving
    #print(f'current stop passenger diff {p_current}')
    p_existing += p_current
    #print(f'Total passenger {p_existing}')

    maximum = max(p_existing,maximum)
    #print(f'Highest so far: {maximum}')
print(maximum)
    