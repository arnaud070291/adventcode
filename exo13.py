#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 10:26:02 2023

@author: ahemmendinger
"""

lettres = 'abcdefghijklmnopqrstuvwxyz0123456789' 


import numpy as np
def retourne(pattern) : 
    pattern = [[a for a in line] for line in pattern.split('\n') if line]
    pattern = np.array(pattern).T
    pattern = '\n'.join([''.join(line) for line in pattern])
    return pattern
    



def to_letters(pattern) : 
    i = 0
    L = []
    DIC = {}
    for line in pattern.split('\n') : 
        if not line : continue
        if line not in DIC : 
            DIC[line] = lettres[i]
            i+=1
        L.append(DIC[line])
        
    letters = "".join(L)
    return letters



def find_reflexion(mot, exception = -1) : 
    #print(mot)
    somme = 0
    for i in range(len(mot)) : 
        new_mot = mot[i:]
        if len(new_mot) == 0 : continue
        if len(new_mot)%2 == 1 : continue
        if new_mot == new_mot[::-1] and  len(new_mot)//2 + i != exception :
            #print(i, new_mot, "supp gauche")
            return len(new_mot)//2 + i
    for i in reversed(range(len(mot))) : 
        new_mot = mot[:i]
        if len(new_mot) == 0 : continue
        if len(new_mot)%2 == 1 : continue
        if new_mot == new_mot[::-1] and  len(new_mot)//2!=exception  :
            #print(i, new_mot, "supp droite")
            return  len(new_mot)//2
    return somme



def process(inp) :
    mot = to_letters(inp)
    r = find_reflexion(mot) 
    if r > 0 : return 100*r
    inp = retourne(inp)
    mot = to_letters(inp)
    r = find_reflexion(mot)
    assert r > 0 
    return r



with open("./input13.txt") as fp:
    INPUT = fp.read().split('\n')

INPUT = ('\n'.join([a if a else "@" for a in INPUT])).split('@')

somme = 0
for inp in INPUT : 
    if not inp : continue
    somme += process(inp)

print(somme)
    
    
    
OTHER = {"#" : ".", "." : "#"}

def fix_smudge(inp, i) : 
    inp_new = [x for x in inp]
    inp_new[i] = OTHER[inp_new[i]]
    return "".join(inp_new)


INPUT_ = [inp]

total_somme = 0
for inp in INPUT : 
    if not inp : continue
    inp = inp.lstrip('\n').rstrip('\n')
    mot = to_letters(inp)
    old_somme = find_reflexion(mot)
    horizontal = True
    for i in range(len(inp)) : 
        if inp[i] not in OTHER : continue
        new_inp = fix_smudge(inp,i)
        mot = to_letters(new_inp)
        somme = find_reflexion(mot, exception = old_somme)
        if old_somme != somme and somme > 0  : 
            total_somme += 100*somme
            break
    else :
        horizontal = False
        
    if horizontal : continue
    
    inp2 = retourne(inp)
    mot = to_letters(inp2)
    old_somme2 = find_reflexion(mot)
    assert old_somme * old_somme2 == 0
    horizontal = True
    for i in range(len(inp2)) : 
        if inp2[i] not in OTHER : continue
        new_inp = fix_smudge(inp2,i)
        mot = to_letters(new_inp)
        somme = find_reflexion(mot, exception = old_somme2)
        if old_somme2 != somme and somme > 0  : 
            total_somme += somme
            break
    else : 
        assert 0 
print(total_somme)


