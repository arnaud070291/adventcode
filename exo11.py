#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 07:22:48 2023

@author: ahemmendinger
"""

import re
import itertools as it
import math
import numpy as np
with open("./input11.txt") as fp:
    INPUT_ = fp.read().split('\n')



INPUT_ = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".split("\n")

INPUT_ = [[i for i in inp] for inp in INPUT_ if inp]   
INPUT_ = np.array(INPUT_)
shape_x, shape_y = INPUT_.shape
# Partie 1 

INPUT =  np.zeros((shape_x+2,shape_y+2),dtype="str")
INPUT[:,:] = "_"
INPUT[1:-1,1:-1]=INPUT_

for i in range(INPUT.shape[0]) : 
    if np.all(INPUT[i] != "#") and np.any(INPUT[i] == "."): 
        INPUT[i][0] = "@"
    

for j in range(INPUT.shape[1]) : 
    if np.all(INPUT[:,j] != "#") and np.any(INPUT[:,j] == "."): 
        INPUT[:,j][0] = "@"


while True : 
    for i in range(INPUT.shape[0]) : 
        if INPUT[i][0] == "@" : 
            INPUT = np.insert(INPUT,i+1,".",axis=0)
            assert INPUT[i,0] == "@"
            INPUT[i,0] = "_"
    for j in range(INPUT.shape[1]) : 
        if INPUT[0,j] == "@" : 
            INPUT = np.insert(INPUT,j+1,".",axis=1)
            assert INPUT[0,j] == "@"
            INPUT[0,j] = "_"
        
    if np.all(INPUT!="@") : 
        break
    
INPUT = INPUT[1:-1,1:-1]



somme = 0
galaxies = [(x,y) for (x,y) in zip(np.where(INPUT=="#")[0],np.where(INPUT=="#")[1])]


for x,y in galaxies : 
    for u,v in galaxies : 
        somme += abs(u-x) + abs(v-y)
print(somme/2)

# Partie 2 
INPUT = INPUT_[:]
expand_x = []
expand_y = []

for i in range(shape_x) : 
    if np.all(INPUT[i] != "#")  : expand_x.append(i)
for j in range(shape_y) : 
    if np.all(INPUT[:,j] != "#")  : expand_y.append(j) 
    
    
    
    
somme = 0
galaxies = [(x,y) for (x,y) in zip(np.where(INPUT=="#")[0],np.where(INPUT=="#")[1])]

expand = 1_000_000
import itertools 
for (x,y),(u,v) in itertools.combinations(galaxies, r = 2) : 
    A= ((x,y),(u,v))
    dist = 0
    if x < u : 
        for i in expand_x : 
            
            if x < i < u : 
                dist += expand - 1
    if u < x : 
        for i in expand_x :
            
            if u < i < x : 
                dist += expand - 1        
    if y < v : 
        for j in expand_y : 
            if y < j < v : 
                dist += expand - 1
    if v < y : 
        for j in expand_y : 
            
            if v < j < y : 
                dist += expand - 1    
    dist = dist + abs(u-x) + abs(v-y)
    somme+= dist
print(somme)
