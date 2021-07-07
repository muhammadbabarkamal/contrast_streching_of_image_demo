# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 05:41:18 2019

@author: muhammad babar
"""
import keras
import random
w=7 \\image width
h=7 \\ image height
img = [[0 for x in range(w)] for y in range(h)] 
img1 = [[0 for x in range(w)] for y in range(h)] 
for x in range(len(img)):
    for y in range(len(img[x])):
        img[x][y]= random.randint(10,100)

minval=min([min(r) for r in img])
maxval=max([max(r) for r in img])

for x in range(len(img)):
    for y in range(len(img[x])):
        img1[x][y]=int(255*((img[x][y]-minval)/(maxval-minval)))