import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Basic conditions
set_speed = 25
u = 0.00
v = 0.00
t = 0.00
dt = 0.1
m = 700
k = 0.5 * 0.24 * 1.225 * 5
Fp = 3000

#Controller variables
Kp = 0.030 #Coefficient of proportion control
Ki = 0.0009 #Coefficient of integral control
Kd = 5  #Coefficient of differentiation control
error =0.00 #set_speed - v
I = 0.00 #error * dt  #Accumulation for integral control
last_error =0.00 #error
t_final = 1200 #Total length of time

#Plotting variables
ulist=[]
vlist=[]
tlist=[]
elist=[]
clist=[]

#Define functions
#Controlle
def DControl(last_error, error):
    return (error - last_error) / dt
def IControl(I, error):
    return I + error * dt

#Relate u to dvdt
def dvdt(u, v):
    return (Fp * u - k * (v ** 2)) / m
#Correct u's range
def correct(u):
    if u > 1.00:
        u = 1.00
    if u < -0.50:
        u = -0.50
    return u

def plotNormal():
    plt.subplot(1, 2, 1)
    plt.ylabel('Velovity m/s')
    plt.xlabel('Time/s')
    plt.plot(tlist, vlist, label='Actual speed', color='000000')
    plt.plot(tlist, clist, label='Set speed', linestyle='--', color='red')

    plt.subplot(1, 2, 2)
    plt.ylabel('Gas padel/%')
    plt.xlabel('Time/s')
    plt.plot(tlist, ulist, color='blue')
    plt.legend
    plt.show()

def plotAni():
    plt.ion()
    plt.subplot(1, 2, 1)
    plt.ylabel('Velovity m/s')
    plt.xlabel('Time/s')
    plt.plot(tlist, vlist, label='Actual speed',color='000000')
    plt.plot(tlist, clist, label='Set speed', linestyle='--',color='red')

    plt.subplot(1, 2, 2)
    plt.ylabel('Gas padel/%')
    plt.xlabel('Time/s')
    plt.plot(tlist, ulist,color='blue')
    plt.legend
    plt.pause(0.01)

aniflag = False
#Main program starts
if str(input('Key in y to draw animated graph: ')) == 'y':
    aniflag = True
else:
    if str(input) == '':
        aniflag = False

while t <= t_final:
    error = set_speed - v
    I = IControl(I,error)
    u = Kp * error + Ki * I #+ Kd * DControl(last_error, error)
    u = correct(u)
    v += dt * dvdt(u, v)
    vlist.append(v)
    ulist.append(u)
    last_error = error
    t += dt
    tlist.append(t)
    clist.append(set_speed)
    if t >= 180.0:
        set_speed = 5
    if t >= 300.0:
        set_speed = 30
    if t >= 700:
        set_speed = 6
    if aniflag == True:
        plotAni()

plotNormal()
# MaxV = 0.00
# Stable = 0.00
# k = 0.00
# Time = 0.00
# for i in range (0,3001):
#     if vlist[i] > MaxV:
#         MaxV = vlist[i]
#     Overshoot=MaxV-set_speed
# print('Overshoot = ' + str(Overshoot))