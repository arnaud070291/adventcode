#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:05:35 2023

@author: ahemmendinger
"""


inp = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".split('\n')

with open("./input5.txt") as fp:
    inp = fp.readlines()
import numpy as np
import re



import re

seeds = list(map(int,re.findall('[0-9]+',inp[0])))

MAPS = []
NEW = []
for line in inp[1:]:
    if re.findall("[a-z]+",line) :
        NEW = []
        continue
    if re.findall("[0-9]+",line) : 
        numbers = list(map(int,re.findall('[0-9]+',line)))
        NEW.append(numbers)
        continue
    else : 
        MAPS.append(NEW)
        continue
    
MAPS.append(NEW)
        
MAPS= MAPS[1:]


## Part 1 


res = []
for seed in seeds : 
    for MAP in MAPS : 
        for L in MAP :
            target,source,length = L
            if source <= seed < source + length : 
                seed = target + (seed-source)
                break
    res.append(seed)
print(min(res))



## Part 2
ALL_SEEDS = []
for seed, length in zip(seeds[::2],seeds[1::2]) : 
    SEED = [[seed, seed + length]]
    for MAP in MAPS : 
        #MAP = sorted(MAP, key = lambda x : x[1])
        ## SPLIT
        SPLIT_LIST = SEED.copy()
        for i in range(100) : 
            NEW_SPLIT = []
            for (seed_debut, seed_fin) in SPLIT_LIST : 
                for L in MAP :
                    target,source,length = L
                    if source<=seed_debut<source+length : 
                        if seed_fin <= source+length : 
                            
                            NEW_SPLIT.append([seed_debut, seed_fin])
                        else : 
                            NEW_SPLIT.append([seed_debut, source + length])
                            NEW_SPLIT.append([source+length, seed_fin])
                        break
                else : 
                    NEW_SPLIT.append([seed_debut,seed_fin])
            SPLIT_LIST = NEW_SPLIT.copy()
        
        ## FORWARD 
        
        NEW_SEED = []
        for (seed_debut, seed_fin) in SPLIT_LIST : 
            for L in MAP:  
                target,source,length = L
                if source<=seed_debut<source+length :
                    NEW_SEED.append([target + (seed_debut - source), target + (seed_fin - source)])
                    break
            else : 
                NEW_SEED.append([seed_debut, seed_fin])
        SEED = NEW_SEED.copy()
    ALL_SEEDS += SEED
        
MIN_SEEDS = [m[0] for m in ALL_SEEDS]
print(min(MIN_SEEDS))


        
    