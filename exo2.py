#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 08:59:56 2023

@author: ahemmendinger
"""

with open("./input2.txt") as fp:
    lines = fp.readlines()
R = 12
G = 13
B = 14


import re, time
t0 = time.time()
somme = 0
for r in lines : 
    if any(list(map(lambda x : int(x)>G,re.findall("([0-9]+) green", r)))):
        continue
    if any(list(map(lambda x : int(x)>R,re.findall("([0-9]+) red", r)))):
        continue
    if any(list(map(lambda x : int(x)>B,re.findall("([0-9]+) blue", r)))):
        continue
    game_num = int(re.findall("Game ([0-9]+)",r)[0])
    somme+=game_num
print(somme,time.time()-t0)

t0 = time.time()
somme = 0
for r in lines : 
    mg=max(map(int,re.findall("([0-9]+) green", r)))
    mr=max(map(int,re.findall("([0-9]+) red", r)))
    mb=max(map(int,re.findall("([0-9]+) blue", r)))
    somme+=mg*mr*mb
print(somme,time.time()-t0)