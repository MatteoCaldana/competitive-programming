# -*- coding: utf-8 -*-

coins = [1, 2, 5, 10, 20, 50, 100, 200]

target = 200

table = [set(), set([(1,)])]
           
def recursive_table(target):
    global table
    for i in range(2,target+1):
        print(i)
        table.append(set())
        for j in coins:
            if i - j > 0:
                for k in table[i - j]:
                    tmp = list(k)
                    tmp.append(j)
                    tmp.sort() # avoid permutations
                    table[i].add(tuple(tmp))
            elif i == j:
                table[i].add(tuple([j]))
    return
        

recursive_table(target)
#print([list(i) for i in table])