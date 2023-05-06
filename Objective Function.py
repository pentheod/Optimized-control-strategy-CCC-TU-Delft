# -*- coding: utf-8 -*-
"""
Created on Sat May  6 20:54:11 2023

@author: penth
"""

import rhinoscriptsyntax as rs

#mode == 0: presentation
#mode == 1: meeting
#mode ==2: workshop
#minlim: minimum limit (target value) for horizontal illuminance at the workplane


minlim = 0

if mode == 0:
    minlim = 300
elif mode == 1:
    minlim = 500 
elif mode == 2:
    minlim = 750

final_incr_n = []
final_incr_s = []
final_incr_w = []
final_incr_e = []
final_angle_n = []
final_angle_s = []
final_angle_w = []
final_angle_e = []


while len(Ecyl) <= 20:    #Running the optimization until the number of iterations reaches 20
    if mode == 0:    #Presentation mode
        for i in Ewp:
        index = Ewp.index(i)
        j = Ecyl[index]
        if i >= minlim and j <= 1400:   
            pen = 1
        elif i < minlim and j < 1400: 
            pen = 10
        else:
            pen = 100
        ObjFun = pen * j  
    else:     #Meeting/Workshop mode
        for i in Ewp:
        index = Ewp.index(i)
        j = Ecyl[index]
        if i >= minlim and j <= 1400:   
            pen = 10
        elif i < minlim and j < 1400: 
            pen = 1
        else:
            pen = -100
        ObjFun = - pen * j  
if len(Ecyl) == 21:    #End of optimization 
    if mode == 0:    #Presentation mode
        min_Ecyl = min(Ecyl)
        index2 = Ecyl.index(min_Ecyl)
        min_Ewp = Ewp[index2]
    else:
        max_Ecyl = max(Ecyl)
        index2 = Ecyl.index(max_Ecyl)
        max_Ewp = Ewp[index2]
    final_incr_n.append(incr_n[index2])
    final_incr_s.append(incr_s[index2])
    final_incr_w.append(incr_w[index2])
    final_incr_e.append(incr_e[index2])
    final_angle_n.append(incr_n[index2])
    final_angle_s.append(incr_s[index2])
    final_angle_w.append(incr_w[index2])
    final_angle_e.append(incr_e[index2])