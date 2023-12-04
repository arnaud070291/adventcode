#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 10:10:18 2023

@author: ahemmendinger
"""

with open("./input3.txt") as fp:
    lines = fp.readlines()
import numpy as np
import re

lines = '''
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''.split()

lines = [[c for c in l.strip("\n")] for l in lines]



A = np.array(lines)
shape_x,shape_y = A.shape
B=  np.zeros((shape_x+2,shape_y+2),dtype="str")
B[:,:] = "."
B[1:-1,1:-1]=A
CHARACTERS = set({"0","1","2","3","4","5","6","7","8","9","."})

### part1 

def test(i,j) : 
    if B[i-1,j] not in CHARACTERS : return True
    if B[i-1,j+1] not in CHARACTERS : return True
    if B[i-1,j-1] not in CHARACTERS : return True
    if B[i,j+1] not in CHARACTERS : return True
    if B[i,j-1] not in CHARACTERS : return True
    if B[i+1,j] not in CHARACTERS : return True
    if B[i+1,j+1] not in CHARACTERS : return True
    if B[i+1,j-1] not in CHARACTERS : return True
    return False

somme=0
for i in range(shape_x+2):
    ligne = "".join(B[i])
    L = [(m.start(0), m.end(0)) for m in re.finditer("[0-9]+",  ligne)]        
    for it in L : 
        a,b = list(it)
        if any([test(i,j) for j in range(*it)]) : 
            somme+=int(ligne[a:b])
    
    
### part2


def test(i,j) : 
    L= []
    if B[i-1,j] == "*" : L.append((i-1,j))
    if B[i-1,j+1] == "*" : L.append((i-1,j+1))
    if B[i-1,j-1] == "*" : L.append((i-1,j-1))
    if B[i,j+1] == "*" : L.append((i,j+1))
    if B[i,j-1] == "*" : L.append((i,j-1))
    if B[i+1,j] == "*" : L.append((i+1,j))
    if B[i+1,j+1] == "*" : L.append((i+1,j+1))
    if B[i+1,j-1] == "*" : L.append((i+1,j-1))
    return list(set(["_".join([str(i),str(j)]) for (i,j) in L]))


res = []
for i in range(shape_x+2):
    ligne = "".join(B[i])
    L = [(m.start(0), m.end(0)) for m in re.finditer("[0-9]+",  ligne)]        
    for it in L : 
        a,b = list(it)
        num = int(ligne[a:b])
        for j in range(*it) : 
            etoiles = test(i,j)
            for etoile in etoiles: 
                res.append([num, etoile])

res2 = {}
for a,b in res : 
    if b not in res2 : 
        res2[b] = set()
        
    res2[b].add(a)
    
somme = 0
for a, L in res2.items() : 
    if len(L)== 2 : 
        a,b = list(L)
        somme+=a*b
    