# Author MB 03/21/2022

def solution(n,d):
    table = list(str(n))
    for i,v in enumerate(table):
            table[i] = int(v)
    if d > len(table):
        return table
    elif d <= 0:
        return []
    else:
        return table[-d:]
            
print(solution(1,1) == [1])
