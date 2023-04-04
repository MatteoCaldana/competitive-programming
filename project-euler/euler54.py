# -*- coding: utf-8 -*-

from collections import Counter   

def eval_card(c):
    suit = c[-1]
    val = c[:-1]
    try:
        val = int(val) - 1
    except ValueError:
        if val == 'T':
            val = 9
        elif val == 'J':
            val = 10
        elif val == 'Q':
            val = 11
        elif val == 'K':
            val = 12
        elif val == 'A':
            val = 13
        else:
            raise ValueError(val)
    return (val, suit)
    
def eval_hand(h):
    h = [eval_card(c) for c in h]
    h.sort(key=lambda x: x[0])
    
    RF, h = royal_flush(h)
    SF, h = straight_flush(h)
    FK, h = four_of_kind(h)
    FH, h = full_house(h)
    F, h = flush(h)
    S, h = straight(h)
    TK, h = three_of_kind(h)
    P, h = pairs(h)
    H = high_card(h)
    
    #print("   RF   SF   FK   FH    F    S   TK    P    H")
    #print("".join(["{:5d}"]*9).format(RF,SF,FK,FH,F,S,TK,P,H))
    
    return(H + P*14 + TK*14**3 + S*14**4 + F*14**5 + FH*14**6 + FK*14**8 + 
           SF*14**9 + RF*14**10)

###############################################################################
# assuming h is sorted, returns cards left in the hand after that evaluation 
# value of the combination is 1-14, 0 means that that combination is not found
###############################################################################

def high_card(h):
    if len(h) == 0:
        return 0
    return max([i[0] for i in h])

def pairs(h):
    tmp = Counter([i[0] for i in h])
    n_pairs = Counter(tmp.values())[2]
    if n_pairs == 0: # there are not any pairs
        return 0, h
    if n_pairs == 1:
        for i in tmp:
            if tmp[i] == 2: #if it is a pair (we already check it exists and is unique)
                return i, [j for j in h if j[0] != i]
    res = []
    for i in tmp:
        if tmp[i] == 2: #if it is a pair
            res.append(i)
            h = [j for j in h if j[0] != i]
    res.sort()
    return sum([res[i]*14**i for i in range(len(res))]), h

def three_of_kind(h):
    tmp = Counter([i[0] for i in h])
    n_triplets = Counter(tmp.values())[3]
    if n_triplets == 0: # there are not any pairs
        return 0, h
    for i in tmp:
        if tmp[i] == 3: #if it is a triplet (we already check it exists and is unique)
            return i, [j for j in h if j[0] != i]
        
def full_house(h):
    original = h
    t1, h = three_of_kind(h)
    t2, h = pairs(h)
    if t1*t2:
        return t1*14 + t2, h
    return 0, original
        
def four_of_kind(h):
    if len(h) < 4:
        return 0, h
    for i in range(2,4):
        if h[1][0] != h[i][0]:
            return 0, h
    if h[0][0] == h[1][0]:
        return h[0][0], h[:-1]
    if len(h) == 5 and h[1][0] == h[4][0]:
        return h[1][0], h[1:]
    return 0, h
        
def straight(h):
    if len(h) < 5:
        return 0, h
    for i in range(4):
        if h[i][0] + 1 != h[i+1][0]:
            return 0, h
        
    return h[0][0], []

def flush(h):
    if len(h) < 5:
        return 0, h
    for i in range(4):
        if h[0][-1] != h[i+1][-1]:
            return 0, h
    
    return 1, []

def straight_flush(h):
    if len(h) < 5:
        return 0, h
    for i in range(4):
        if h[i][0] + 1 != h[i+1][0] or h[i][1] != h[i+1][1]:
            return 0, h
        
    return h[0][0], []

def royal_flush(h):
    if h[0][0] != 9:
        return 0, h
    return straight_flush(h)

###############################################################################
    
tests = ["5H 5C 6S 7S KD 2C 3S 8S 8D TD", "5D 8C 9S JS AC 2C 5C 7D 8S QH",
         "2D 9C AS AH AC 3D 6D 7D TD QD","4D 6S 9H QH QC 3D 6D 7H QD QS",
         "2H 2D 4C 4D 4S 3C 3D 3S 9S 9D"]

def test_to_hand(t):
    tmp = t.split(' ')
    return tmp[:5], tmp[5:]

def run_test(t):
    h1, h2 = test_to_hand(t)
    v1 = eval_hand(h1)
    v2 = eval_hand(h2)
    if v1 > v2:
        #print('P1',v1, v2)
        return 1
    else:
        #print('P2',v1, v2)
        return 0

for i in tests:
    run_test(i)
    
with open("p054_poker.txt", 'r') as f:
    data = f.read()
    
data = data.split('\n')[:-1]
p1_wins = 0
for i in data:
    p1_wins += run_test(i)















    