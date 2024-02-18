tic_tac_toe = []
for _ in range(3):
    letters = list(map(str,input().split()))
   # print(letters)
    tic_tac_toe.append(letters)

#print(tic_tac_toe)
def get_victory(n):
    common = set()
    for l in tic_tac_toe:
        if len(set(l[0])) == n:
            common.add(''.join(l[0]))
    
    for j in range(3):
        col = [tic_tac_toe[0][0][j],tic_tac_toe[1][0][j],tic_tac_toe[2][0][j]]
        if len(set(col)) == n:
            common.add(''.join(col))
    l_diag = set()
    r_diag = set()
    for i in range(3):
        l_diag.add(tic_tac_toe[i][0][i])
        r_diag.add(tic_tac_toe[i][0][2-i])

    
    if len(l_diag) == n:
        l_diag = ''.join(list(l_diag))
        common.add(l_diag)

    if len(r_diag) == n:
        r_diag = ''.join(list(r_diag))
        common.add(r_diag)
    #print(common)
    print(len(common))

get_victory(1)
get_victory(2)

