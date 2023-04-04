import os
import sys
from bisect import bisect

# leaderboard[i] == index in scores of the first score in (i-th + 1) position
def evalScoreboard(scores):
    leaderboard = [0]

    i = 1
    while True:
        while (i < len(scores)) and (scores[i] == scores[leaderboard[-1]]):
            i += 1
        if i >= len(scores):
            break
        leaderboard.append(i)

    leaderboard.append(len(scores))
    return leaderboard

def revbisect(l,x):
    lo = len(l)
    hi = 0
    while hi < lo:
        mid = (lo+hi)//2
        if x < l[mid]: hi = mid + 1
        else: lo = mid
    return lo

def updateScoreboard(scores, leaderboard, newScore, times=1):
    idx = revbisect(scores, newScore)
    pos = bisect(leaderboard, idx)

    #for i in range(times):
    #    scores = scores.insert(idx, newScore)
#
    #for i in range(pos,len(leaderboard)):
    #    leaderboard[i] += times

    return pos

def climbingLeaderboard(scores, alice):
    leaderboard = evalScoreboard(scores)

    result = []
    for i in range(len(alice)):
        score = alice[i]
        pos = updateScoreboard(scores, leaderboard, score)
        result.append(pos)
    return result

def isSorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True
        
#scores = [100, 100, 50, 40, 40, 20, 10]
#alice = [5, 25, 50, 120]
#
#scores = [100, 90, 90, 80, 75, 60]
#alice = [50, 65, 77, 90, 102] 

with open("climbing-the-leaderboard_input06.txt",'r') as f:
    data = f.read()
data = data.split('\n')
scores = [int(i) for i in data[1].split(' ')]
alice = [int(i) for i in data[3].split(' ')]
print(isSorted(alice))
print(len(scores), len(alice))
result = climbingLeaderboard(scores, alice)


with open("climbing-the-leaderboard_output06.txt",'r') as f:
    res = f.read()
res = [int(i) for i in res.split('\n')]
print(result == res)