import rhinoscriptsyntax as rs
#Inputs:
#Ewp = list of average workplane illuminances calculated during optimization's iterations
#Ecyl = list of maximum cylindrical illuminances calculated during optimization's iterations
#mode = activity mode (presentation, meeting, workshop)
#incr_n = list of North blinds' increments tested during optimization's iterations
#incr_s = list of South blinds' increments tested during optimization's iterations
#incr_e = list of East blinds' increments tested during optimization's iterations
#incr_w = list of West blinds' increments tested during optimization's iterations
#angle_n = list of North blinds' angles tested during optimization's iterations
#angle_s = list of South blinds' angles tested during optimization's iterations
#angle_e = list of East blinds' angles tested during optimization's iterations
#angle_w = list of West blinds' angles tested during optimization's iterations
#Nol = number of luminaires
#Lumfl = luminous flux per luminaire (lm)
#P = power per luminaire (W)
#A = floor area

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
        if min_Ewp < minlim: 
            light_intensity = A * (minlim - min_Ewp) / (Nol * Lumfl)
            light_dim_level = math.ceil(light_intensity * 10) / 10
            Electricity = light_dim_level * Nol * P * 0.001 /4  #kWh
        else:
            light_dim_level = 0
            Electricity = 0
    else:
        final_Ecyl = max(Ecyl)    #best value of Ecyl
        index2 = Ecyl.index(final_Ecyl)
        final_Ewp = Ewp[index2]   #best value of Ewp
        if min_Ewp < minlim: 
            light_intensity = A * (minlim - min_Ewp) / (Nol * Lumfl)
            light_dim_level = math.ceil(light_intensity * 10) / 10
            Electricity = light_dim_level * Nol * P * 0.001 /4  #kWh
        else:
            light_dim_level = 0
            Electricity = 0 
    final_incr_n = incr_n[index2]
    final_incr_s = incr_s[index2]
    final_incr_w = incr_w[index2]
    final_incr_e = incr_e[index2]
    final_angle_n = angle_n[index2]
    final_angle_s = angle_s[index2]
    final_angle_w = angle_w[index2]
    final_angle_e = angle_e[index2]
