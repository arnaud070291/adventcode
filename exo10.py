#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:22:35 2023

@author: ahemmendinger
"""

import re
import itertools as it
import math
import numpy as np
with open("./input10.txt") as fp:
    INPUT_ = fp.read().split('\n')
    INPUT_ = [[i for i in inp] for inp in INPUT_ if inp]
INPUT_ = np.array(INPUT_)


PIPES_CONNECTION = {"|" : {"N" : ["|", "F", "7"], "S" : ["|","L","J"]},
                    "-" : {"W" : ["-", "L", "F"], "E" : ["-", "J","7"]},
                    "L" : {"E" : ["-", "7","J"], "N" : ["|", "F", "7"]},
                    "7" : {"W" : ["-","L", "F"], "S" : ["|", "L", "J"]},
                    "J" : {"W" : ["-", "F","L"], "N" : ["|", "F", "7"]},
                    "F" : {"S" : ["|", "J", "L"], "E" : ["-", "J", "7"]}
                    }


shape_x, shape_y = INPUT_.shape
INPUT =  np.zeros((shape_x+2,shape_y+2),dtype="str")
INPUT[:,:] = "."
INPUT[1:-1,1:-1]=INPUT_
set_index = set()
depart_index  = np.where(INPUT=="S")
depart_index = [int(depart_index[0]), int(depart_index[1])]

# trouver bon caractère pour le start
i_start,j_start = depart_index
adjacents = [(i_start+i,j_start+j,direction) for (i,j,direction) in [(0,1,"E"),(0,-1,"W"),(-1,0,"N"),(1,0,"S")]]
for character in PIPES_CONNECTION : 
    if sum([INPUT[i,j] in PIPES_CONNECTION[character][direction] for (i,j,direction) in adjacents
                          if direction in PIPES_CONNECTION[character]]) == 2 :
        START_CHARACTER = character

INPUT[*depart_index] = START_CHARACTER
    
# Partie 1

def transform_index(x,y) : 
    return "_".join([str(x),str(y)])

str_depart_index = transform_index(*depart_index)
set_index.add(str_depart_index)

current_index = str_depart_index
current_character = START_CHARACTER


while True :
    ending = True
    for (i,j,direction) in [(0,1,"E"),(0,-1,"W"),(-1,0,"N"),(1,0,"S")]  : 
        ind_i, ind_j = map(int, current_index.split("_"))
        if direction in PIPES_CONNECTION[current_character] :
            
            if INPUT[ind_i + i,ind_j + j] in PIPES_CONNECTION[current_character][direction] : 
                new_index = transform_index(ind_i + i,ind_j+j)
                if new_index not in set_index : 
                    set_index.add(new_index)
                    current_index = new_index
                    current_character = INPUT[ind_i + i,ind_j + j]
                    ending = False
    if ending : break
            
print(len(set_index)/2)




# Part 2 

str_depart_index = transform_index(*depart_index)
set_index.add(str_depart_index)

current_index = str_depart_index
current_character = START_CHARACTER

PATH = []


while True :
    ending = True
    for (i,j,direction) in [(0,1,"E"),(0,-1,"W"),(-1,0,"N"),(1,0,"S")]  : 
        ind_i, ind_j = map(int, current_index.split("_"))
        if direction in PIPES_CONNECTION[current_character] :
            
            if INPUT[ind_i + i,ind_j + j] in PIPES_CONNECTION[current_character][direction] : 
                new_index = transform_index(ind_i + i,ind_j+j)
                if new_index not in PATH : 
                    PATH.append(new_index)
                    current_index = new_index
                    current_character = INPUT[ind_i + i,ind_j + j]
                    ending = False
                    print(current_character, current_index)
    if ending : break


PATH  = [ list(map(int, point.split("_"))) for point in PATH]

RANGE_X = {}
for point in PATH : 
    i,j = point
    if i not in RANGE_X: 
        RANGE_X[i] = [100_000_000,-1] 
    if j > RANGE_X[i][1] : 
        RANGE_X[i][1] = j
    if j < RANGE_X[i][0] : 
        RANGE_X[i][0] = j+1
        

TEST_POINTS = []
for i in RANGE_X : 
    for j in range(*RANGE_X[i]) : 
        if [i,j] in PATH : continue
        TEST_POINTS.append([i,j])
            
            


SEGMENTS = [[point1, point2] for point1,point2 in zip(PATH[:-1],PATH[1:])]
SEGMENTS.append([PATH[-1],PATH[0]])
from scipy.integrate import quad

def calcul(i,j) : 
    CONSTANT = 1/(2*np.pi)
    z0 = j + 1j*i
    somme = 0 
    for (i,j), (k,l) in SEGMENTS : 
        z1 = j + 1j*i
        z2 = l + 1j*k
        dz = z2-z1
        somme += dz*quad(lambda t : 1/(z1 + t*dz - z0), 0,1, complex_func= True)[0]
    return somme/CONSTANT
        
import tqdm
res = []
for (i,j) in tqdm.tqdm(TEST_POINTS) : 
    res+= [calcul(i,j)]
    
print(len([x for x in res if not np.allclose(x,0)]))






        