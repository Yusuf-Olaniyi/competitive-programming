n = int(input())

def numIdenticalPairs(nums):
    n_count = {}  
    good_pairs = 0
    for num in nums:
        if num in n_count:
            n_count[num] += 1
        else:
            n_count[num] = 1
    #print(n_count)
    for count in n_count.values():
        good_pairs += (count * (count - 1)) // 2

    return good_pairs

c_pair = 0
while n > 0:
    nums = list(map(int,input().split()))
    c_pair += numIdenticalPairs(nums)
    n-=1

print(c_pair)




