n = int(input())

for _ in range(n):
    l = int(input())
    elements = list(map(int,input().split()))
    if len(set(elements)) == 1:
        print(0)
    else:
        counter = {}
        for e in elements:
            if e in counter:
                counter[e] += 1
            else:
                counter[e] = 1
        print(counter)
        #if len(set(counter.values())) == 1:
