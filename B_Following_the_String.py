n_test = int(input())

while n_test > 0:
    lenght = int(input())
    lost = list(map(int,input().split()))
    alphabet = [chr(i) for  i in range(97, 123)]
    output = ''
    characters = {}
    for i in range(len(lost)):
        if lost[i] == 0:
            output += alphabet[i]
            characters[alphabet[i]] = 0
            
        else:
            for char in characters:
                if characters[char]+1 == lost[i]:
                    output += char
                    characters[char] += 1
                    break
                    
                

    print(output)


    n_test -= 1