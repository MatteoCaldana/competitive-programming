# -*- coding: utf-8 -*-

def _split_string(string, results, memory=()):
    results.append(tuple([*memory, string]))
    for i in range(1, len(string)):
        _split_string(string[i:], results, tuple([*memory, string[:i]]))
    return

def split_string(string):
    results = []
    _split_string(string, results)
    return results

###############################################################################
    
def _split_string_hint(string, max_len, results, memory=()):
    if len(string) < max_len: results.append(tuple([*memory, string]))
    for i in range(1, len(string)):
        _split_string_hint(string[i:], max_len, results, tuple([*memory, string[:i]]))
    return

def split_string_hint(string, max_len):
    results = []
    _split_string_hint(string, max_len, results)
    return results

###############################################################################
    
def _split_string_nocp(string, max_len, results, current):
    if len(string) < max_len: results.append(tuple(current+[string]))
    for i in range(1, len(string)):
        current.append(string[:i])
        _split_string_nocp(string[i:], max_len, results, current)
        current.pop()
    return

def split_string_nocp(string, max_len):
    results = []
    current = []
    _split_string_nocp(string, max_len, results, current)
    return results

###############################################################################
    
def _split_string_nocp2(string, max_len, num, results, current):
    if len(string) < max_len: results.append(current+[int(string)])
    for i in range(1, min(len(string), max_len)):
        current.append(int(string[:i]))
        if sum(current) < num: 
            _split_string_nocp2(string[i:], max_len, num, results, current)
        current.pop()
    return

def split_string_nocp2(string, max_len, num):
    results = []
    current = []
    _split_string_nocp2(string, max_len, num, results, current)
    return results

###############################################################################
    
def toi(string, st, en):
    exp, res = 1, 0
    for i in range(en-1,st-1,-1):
        res += exp * (ord(string[i]) - ord('0'))
        exp *= 10
    return res
    
def _split_string2(st, en, depth, max_len):
    global string, results, current
    l = en - st
    if l < max_len:
        current[depth] = toi(string, st, en)
        results.append(sum(current))
    for i in range(1, min(l, max_len)):
        current[depth] = toi(string, st, st+i)
        _split_string2(st+i, en, depth+1, max_len)
        current[depth] = 0
    current[depth] = 0
    return

def split_string2(max_len):
    global string, results, current
    results = []
    current = [0]*13
    _split_string2(0, len(string), 0, max_len)
    return results

###############################################################################
    
string = ''
results = []
current = [0]*13 

def is_S(num):
    global string
    string = str(num*num)
    splittings = split_string2(len(str(num))+1)
    for s in splittings:
        if s == num:
            return True
    return False

res = 0
for i in range(10**6, 3, -1):
    if (i % 1000) == 0: print(i)
    if(is_S(i)):
        res += (i*i)