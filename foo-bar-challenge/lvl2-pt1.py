def make_solution(l):
    if len(l) == 0:
        return 0
    sol = ""
    l.sort(reverse=True)
    for n in l:
        sol += str(n)
    return int(sol)
    
def find_smallest_with_reminder(l, rem):
    l.sort()
    for n in l:
        if n % 3 == rem:
            return n
    raise ValueError()
    return -1
    
def find_two_smallest_with_reminder(l, rem):
    l.sort()
    sol = []
    for n in l:
        if n % 3 == rem:
            sol.append(n)
            if len(sol) == 2:
                return sol
    raise ValueError()
    return -1

def solution(l):
    # Your code here
    mods = [i % 3 for i in l]
    reminder = sum(l) % 3 
    if reminder == 0:
        return make_solution(l)
    else:
        if len([m for m in mods if m == reminder]):
            l.remove(find_smallest_with_reminder(l,reminder))
            return make_solution(l)
        else:
            two_smallest = find_two_smallest_with_reminder(l, 3-reminder)
            l.remove(two_smallest[0])
            l.remove(two_smallest[1])
            return make_solution(l)

s = solution([5,7,1,8])
