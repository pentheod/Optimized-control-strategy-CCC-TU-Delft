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
else:    #End of optimization 
    if mode == 0:    #Presentation mode
        final_Ecyl = min(Ecyl)   #best value of Ecyl
        index2 = Ecyl.index(final_Ecyl)
        final_Ewp = Ewp[index2]   #best value of Ewp
    else:
        final_Ecyl = max(Ecyl)    #best value of Ecyl
        index2 = Ecyl.index(final_Ecyl)
        final_Ewp = Ewp[index2]   #best value of Ewp
    final_incr_n = incr_n[index2]
    final_incr_s = incr_s[index2]
    final_incr_w = incr_w[index2]
    final_incr_e = incr_e[index2]
    final_angle_n = incr_n[index2]
    final_angle_s = incr_s[index2]
    final_angle_w = incr_w[index2]
    final_angle_e = incr_e[index2]
