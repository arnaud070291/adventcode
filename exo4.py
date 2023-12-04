#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 10:12:18 2023

@author: ahemmendinger
"""

with open("./input4.txt") as fp:
    lines = fp.readlines()
import numpy as np
import re


lines = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split('\n')

# part1
somme = 0
for line in lines : 
    line = line.split(':')[1]
    gauche, droite = line.split('|')
    nombres_g = re.findall('[0-9]+',gauche)
    nombres_d = re.findall('[0-9]+',droite)
    length = len(set(nombres_g).intersection(set(nombres_d)))
    somme += (length >0)*2**(length - 1)
    
# part2
CARDS = {}
for i,line in enumerate(lines) : 
    line = line.split(':')[1]
    gauche, droite = line.split('|')
    nombres_g = re.findall('[0-9]+',gauche)
    nombres_d = re.findall('[0-9]+',droite)
    length = len(set(nombres_g).intersection(set(nombres_d)))
    CARDS[i+1] = length
    
SUMS = {i : 1 for i in range(1,len(lines)+1)}
for i in range(1,len(lines)+1) : 
    for j in range(1,CARDS[i]+1):
        SUMS[j+i]+=SUMS[i]

sum(SUMS.values())
