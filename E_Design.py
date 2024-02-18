n,q = tuple(map(int,input().split()))
words = []
queries = []
for _ in range(n):
    word = input()
    words.append(word)

for _ in range(q):
    query = input()
    queries.append(query)

for query in queries:
    index = -1
    pref,suff = query[0],query[-1]
    for i in range(len(words)):
        if words[i][0] == pref and words[i][-1] == suff:
            index = i

    print(index)


    
