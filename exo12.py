#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:24:16 2023

@author: ahemmendinger
"""

import re
import itertools as it
import math
import numpy as np
import functools
with open("./input12.txt") as fp:
    INPUT = fp.read().split('\n')
import tqdm


### PARTIE1

somme = 0
for inp in tqdm.tqdm(INPUT) : 
    if not inp : continue
    characters, nombres = inp.split(" ")
    chara_list = list(characters)
    nombres = list(map(int, nombres.split(',')))
    interrogations = [i for i,x in enumerate(characters) if x == "?"]
    for X in it.product(["#","."],repeat = len(interrogations)) : 
        chara_list_copy = chara_list.copy()
        for (i,x) in zip(interrogations, X) : 
            chara_list_copy[i] = x
        chara_list_copy = [len(x) for x in ("".join(chara_list_copy)).split(".") if x]
        if chara_list_copy == nombres : 
            somme+=1
        



### PARTIE2 

def crop(liste, base) : 
    new_liste = liste.copy()
    i = 0
    length = len(base)
    while True : 
        
        if i == length : 
            return new_liste, "", 1*(len(new_liste)==0)
        c = base[i]
        if c == "." : i+=1
        elif c == "?" : return new_liste, base[i:],1
        elif c == "#" : 
            try : 
                assert "." not in base[i:i+new_liste[0]] 
                if i + new_liste[0] < length : 
                    assert base[i + new_liste[0]] != "#"
                    base =  change_string(i + new_liste[0], base, '.') 
                else : 
                    assert i + new_liste[0] == length
            except Exception as e: 
                return [], '', 0
            i+= new_liste[0]
            new_liste.pop(0)

            


    
def change_string(index, old, char) : 
    old = list(old)
    old[index] = char
    return "".join(old)



@functools.lru_cache
def character_liste(liste, base) : 
    BASE = base
    liste = liste.strip()
    if len(liste) == 0 and "#" not in base : return 1
    liste = list(map(int, liste.split('|')))
    
    liste, base, count = crop(liste, base)
    if len(liste) == 0 : 
        if "#" not in base : return 1
        if '#' in base : return 0
    
    if count == 0 : return 0
    
    count = 0
    ## base[0] = #
    new_base = base
    
    
    while True : 
        if len(base) == 1  :
            if liste == [1] : count +=1
            else : count += 0
            break
        
        try :
            length = liste[0] 
        except : 
            
            print(liste, base, count, len(liste))
            DICO.append([liste, base, count, BASE])
            assert 0 
            
            
        if "." in base[:length] : 
            count += 0 
            break
        
        try : 
            if base[length] == "#" : 
                count+=0
                break
        except : pass
        
        try : 
            for i in range(length) : 
                new_base = change_string(i, new_base, "#")
            if length < len(base) :
                new_base = change_string(length,new_base,".")
            new_liste, new_base, count_ = crop(liste, new_base)
            new_liste = '|'.join(map(str,new_liste))
            res = character_liste(new_liste, new_base)
            count += count_*res
            break
        except : 
            count+=0
            break
        
    new_base = base
    ## base[0] = .
    while True : 
        if len(base) == 1  :
            if liste == [] : count +=1
            else : count += 0
            break
        new_base = change_string(0, new_base, ".")
        new_liste, new_base, count_ = crop(liste, new_base)
        new_liste = '|'.join(map(str,new_liste))
        count += count_*character_liste(new_liste, new_base)
        break
    return count
    

    
liste_inputs = ["???.### 1,1,3" ,
                ".??..??...?##. 1,1,3",
                "?#?#?#?#?#?#?#? 1,3,1,6" ,
                "????.#...#... 4,1,1",
                "????.######..#####. 1,6,5" ,
                "?###???????? 3,2,1" 
                ]

[1,16384,1,16,2500,506250]
inp = liste_inputs[0]
import tqdm
somme = 0
for inp in tqdm.tqdm(INPUT) : 
    if not inp : continue
    base, nombres = inp.split(' ')
    liste = list(map(int,nombres.split(',')))*5
    base = ((base+ '?')*5)[:-1]
    liste = '|'.join(map(str,liste))
    c = character_liste(liste, base)
    print(c)
    somme += c
    
print(somme)

    