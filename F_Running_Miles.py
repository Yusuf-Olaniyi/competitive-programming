n_test = int(input())

while n_test > 0:
    n_i = int(input())
    beauty = list(map(int,input().split()))
    beauty_sorted = sorted(beauty)
    #print(beauty_sorted)
    if beauty_sorted[-1] != beauty_sorted[-3]:
        l =  beauty.index(beauty_sorted[-1]) + 1
        r = beauty.index(beauty_sorted[-3]) + 1
    
        print(sum(beauty_sorted[-3:]) - (r - l))
    else: 
        l_r = beauty.count(beauty_sorted[-1])
        print(abs(sum(beauty_sorted[-3:]) - l_r))


    n_test -= 1