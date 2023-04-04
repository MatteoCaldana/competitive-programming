# -*- coding: utf-8 -*-
def build_divisors_table(l):
    table = []
    for i in range(len(l)):
        table.append([])
        for j in range(i+1,len(l)):
            table[i].append(1 if l[j] % l[i] == 0 else 0)
    return table

def count_tripe_starting_idx(idx, table):
    count = 0
    for i in range(len(table[idx])):
        if table[idx][i] == 1:
            row_el2 = idx + i + 1
            count += sum(table[row_el2])
    return count
                

def solution(l):
    if len(l) < 3:
        return 0
    if len(l) == 3:
        if (l[2] % l[1] == 0) and (l[1] % l[0] == 0):
            return 1
        else:
            return 0
    else:
        triples = 0
        table = build_divisors_table(l)
        print(table)
        for i in range(len(table)):
            tmp = count_tripe_starting_idx(i, table)
            triples += tmp
        return triples
    
test1 = [1, 1, 1]
test2 = [1, 2, 3, 4, 5, 6]
test3 = [1, 2, 3, 4, 5, 6, 8]

test = test3  

print(solution(test))