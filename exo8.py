#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:48:29 2023

@author: ahemmendinger
"""

INPUT="""LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".split('\n')
INPUT = [inp for inp in INPUT if inp]

with open("./input8.txt") as fp:
    INPUT = fp.read().split('\n')
    INPUT = [inp for inp in INPUT if inp]
    
import re
import itertools as it
import math
MOUVEMENTS = [re.findall("[0-9A-Z]{3}", x) for x in INPUT[1:]]
DIC_MOUVEMENTS = {a : [b,c] for (a,b,c) in MOUVEMENTS}

## Partie 1 


source = "AAA" 


def find(source, endswith) : 
    res = 0
    for m in it.cycle(INPUT[0]) : 
        res +=1
        match m :
            case "L" : i = 0
            case "R" : i = 1
        source = DIC_MOUVEMENTS[source][i]
        if source.endswith(endswith) : break
    return res
print(find(source,"ZZZ"))


## Partie 2



sources = [k for k in DIC_MOUVEMENTS if k.endswith("A")]
RES = [find(source, "Z") for source in sources]
print(math.lcm(*RES))
