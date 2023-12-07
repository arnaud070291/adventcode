#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 07:23:43 2023

@author: ahemmendinger
"""

import collections



INPUT = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split('\n')


with open("./input7.txt") as fp:
    INPUT = fp.read().split('\n')
    INPUT = [inp for inp in INPUT if inp]

def get_rank(card):
    count = collections.Counter(card)
    count = "".join(map(str,reversed(sorted(count.values()))))
    if count == "5" : 
        rank = 7
    elif count == "41" : 
        rank = 6
    elif count == "32" : 
        rank = 5 
    elif count == "311" : 
        rank = 4 
    elif count == "221" : 
        rank = 3 
    elif count == "2111" : 
        rank = 2
    else : 
        rank = 1
    return rank


## Part 1 


CARDS1 = '23456789TJQKA'


def get_score(card) : 
    rank = get_rank(card)
        
    score = rank*10**20
    for i, c in enumerate(reversed(card)) : 
        score += CARDS1.index(c)*10**(2*i)

    return score


    
    
cards = sorted([line.split(" ") for line in INPUT], key = lambda x : get_score(x[0]))

BID = [(i+1)*int(bid) for i,(card, bid) in enumerate(cards)]
print(sum(BID))



## Part2

import itertools as it


CARDS2 = 'J23456789TQKA'


def get_score2(card) : 
    top_rank = 0
    Js = []
    for i,c in enumerate(card) : 
        if c == "J" : 
            Js.append(i)
    if len(Js) == 0 :
        top_rank = get_rank(card)
    else : 
        L = list(card)
        for REMPLACEMENT in it.product(L, repeat = len(Js)) : 
            L2 = L.copy()
            for i, x in enumerate(REMPLACEMENT) : 
                L2[Js[i]] = x
                
            new_card = "".join(L2)
            rank = get_rank(new_card)
            if rank > top_rank : 
                top_rank = rank
    score = top_rank*10**20
    for i, c in enumerate(reversed(card)) : 
        score += CARDS2.index(c)*10**(2*i)

    return score

    
cards = sorted([line.split(" ") for line in INPUT], key = lambda x : get_score2(x[0]))

BID = [(i+1)*int(bid) for i,(card, bid) in enumerate(cards)]
print(sum(BID))
