n_box = int(input())
boxes = sorted(map(int,input().split()))

#count the maximum consecutive number

prev = 0
count = 1
max_count  = 1

for box in boxes:
    if box == prev:
        count += 1
    else:
        count = 1
    
    max_count = max(max_count,count)

    prev = box

print(max_count)

