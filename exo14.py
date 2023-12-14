#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 10:51:01 2023

@author: ahemmendinger
"""

with open("./input14.txt") as fp:
    INPUT_ = fp.read().split('\n')


INPUT_ = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".split('\n')





import numpy as np

def roll(INPUT,r = 0) :
    for i in range(r) : 
        INPUT = np.rot90(INPUT,-1)
    
    
    somme = 0
    cols = []
    for col in INPUT.T : 
        length = len(col)
        last_character = col[-1]
        col = ''.join(col)
        col = col.replace('#',"_#")
        col = col.split("#")
        for i,part in enumerate(col) : 
            num_O = len([1 for c in part if c == "O"])
            new_part = "O"*num_O + "."*(len(part) - num_O - 1) + "_"
            col[i] = new_part
        col = "".join(col)
        if last_character in ['#',"."]: 
            col = col[:-1] + last_character
            
        if last_character == "O":
            col = col[:-1] + "."
        col = col.replace('_','#')
        col = col[:length]
        cols.append(col)
        for i, c in enumerate(col[::-1]) : 
            
            if c == "O" : 
                somme += 0
    INPUT = np.array([[c for c in col] for col in cols]).T
    for i in range(r) : 
        INPUT = np.rot90(INPUT,1)
    
    for i,L in enumerate(INPUT[::-1]) : 
        num_O = sum([1 for c in L if c == "O"])
        somme += num_O*(i+1)
        
        
        
    return INPUT, somme

def calcul(INPUT) : 
    somme = 0
    for i,L in enumerate(INPUT[::-1]) : 
        num_O = sum([1 for c in L if c == "O"])
        somme += num_O*(i+1)
    return somme 


def to_string(array) : 
    return "".join(["".join([a for a in arr]) for arr in array])
    
    


INPUT_ = np.array([[a for a in L] for L in INPUT_ if L])

all_hashs = []
sommes = []

INPUT = INPUT_[:]

somme = calcul(INPUT)
sommes.append(somme)
hashing = hash(to_string(INPUT))
all_hashs.append(hashing)
patterns = [INPUT]
for i in range(0,250_000) : 
    INPUT,somme_0 = roll(INPUT,i%4)
    hashing = hash(to_string(INPUT))
    somme = calcul(INPUT)
    assert somme_0 == somme
    sommes.append(somme)
    if hashing not in all_hashs : 
        all_hashs.append(hashing)
    else :
        index = all_hashs.index(hashing)
        break

cycle = len(all_hashs) - index
num_tours = 4_000_000_000
n = (num_tours - index)%cycle + index


print(sommes[n])

