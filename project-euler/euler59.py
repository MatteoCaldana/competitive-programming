# -*- coding: utf-8 -*-

with open("p059_cipher.txt", 'r') as f:
    data = f.read()
    
data = [int(i) for i in data.split(',')]


def decrypt(key, data):
    text = [chr(ord(key[i%len(key)])^data[i]) for i in range(len(data))]
    return ''.join(text)

keys = []
for i in range(26):
    for j in range(26):
        for k in range(26):
            keys.append(''.join([chr(i+ord('a')),chr(j+ord('a')),chr(k+ord('a'))]))

res = []
for key in keys:
    text = decrypt(key, data)
    if text != "":
        res.append((key,text))
  
#https://en.wikipedia.org/wiki/Most_common_words_in_English          
common_words = ['be','the','to','of','and','that']

count = 0
for i in range(len(res)):
    found = 0
    for w in common_words:
        if res[i][1].find(w) != -1:
            found += 1
    if found == len(common_words): #possibly: found > len() - slack
        count += 1
        print(res[i], i)
        print("================")
        
result = sum([ord(i) for i in res[3317][1]])
    
    
    