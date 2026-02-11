def calc(expr):
    
    import re
    
    # expr = "345+987"
    part1, part2 = expr.split("+")
    print(part1+ " " + part2)
    print(str(len(part1)) + " " + str(len(part2)))
    temp=[]
    for i in range(len(part1)):
        for j in range(1, len(part2)+1):    
            temp.append( part1[:i] + "(" + part1[i:] + "+" + part2[:j] + ")" + part2[j:] )
    print(temp)
    
    res1=[]
    delimiters_pattern = r'[\(\)]+'
    
    for i in temp:
        res1.append(re.split(delimiters_pattern, i))
    print(res1)
    
    prod = []
    for i in res1:
        n1, n2 = i[1].split("+")
        i[1] = int(n1) + int(n2)
        if i[0] == '':
            i[0] = 1
        else:
            i[0] = int(i[0])
        if i[2] == '':
            i[2] = 1
        else:
            i[2] = int(i[2])
        prod.append( i[0] * i[1] * i[2] )
     
    print(res1)
    print(prod)
    print(min(prod))
    return min(prod)
