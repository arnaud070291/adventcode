#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 08:55:43 2023

@author: ahemmendinger
"""

### Part1 

times = [52,94,75,94]
distances = [426,1374,1279,1216]


times = [7,15,30]
distances = [9,40,200]

produit = 1
for time, d in zip(times, distances) : 
    s = 0
    for t in range(1,time): 
        if t + d/t < time : 
            s+=1
    print(s)
    produit*=s
    



### Part 2

time = 71530
distance = 940200


time = 52947594
distance = 426137412791216




from scipy.optimize import minimize


def f(t) : 
    return (t + distance/t - time)**2


x1 = minimize(f,[1]).x
x2 = distance/x1

x1,x2 = min(x1,x2), max(x1,x2)
x1 = int(x1)+1
x2 = int(x2)


print(x2-x1+1)