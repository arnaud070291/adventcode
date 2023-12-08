#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:48:29 2023

@author: ahemmendinger
"""

import re
import itertools as it
import math
with open("./input8.txt") as fp:
    INPUT = fp.read().split('\n')
    INPUT = [inp for inp in INPUT if inp]
    MOUVEMENTS = [re.findall("[0-9A-Z]{3}", x) for x in INPUT[1:]]
    DIC_MOUVEMENTS = {a : {"L" : b, "R" : c} for (a,b,c) in MOUVEMENTS}

## Partie 1 
def find(source, endswith) : 
    for i, m in enumerate(it.cycle(INPUT[0])) : 
        source = DIC_MOUVEMENTS[source][m]
        if source.endswith(endswith) : break
    return i+1
print(find("AAA","ZZZ"))


## Partie 2
sources = [k for k in DIC_MOUVEMENTS if k.endswith("A")]
RES = [find(source, "Z") for source in sources]
print(math.lcm(*RES))
