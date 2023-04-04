# -*- coding: utf-8 -*-

from utils import index

t = []
for i in range(1,100):
    t.append(i*(i+1)//2)
    
with open("p042_words.txt", 'r') as f:
    data = f.read()
    
words = data.split(',')
words = [word[1:-1] for word in words]

def check_triangle_word(word):
    s = 0
    for letter in word:
        s += ord(letter) - ord('A') + 1
    if index(t, s) != -1:
        return True
    return False

res = []
for word in words:
    if check_triangle_word(word):
        res.append(word)
        
result = len(res)
    