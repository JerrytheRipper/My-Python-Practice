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
Kp = 1 #Coefficient of proportion control
Kd = 0.03 #Coefficient of differentiation control
Ki = 0.065 #Coefficient of integral control
error = set_speed - v
I = error * dt  #Accumulation for integral control
last_error = error
t_final = 60 #Total length of time

#Plotting variables
ulist=[]
vlist=[]
tlist=[]
elist=[]
clist=[]#List for set speed

#Define functions
#Controller
def PControl(v):
    return (set_speed - v)
def DControl(last_error, error):
    return (error - last_error) / dt
def IControl(I, error):
    I = I + error * dt
    return I

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
    plt.plot(tlist, clist, label='Set speed', linestyle='--', color='000000')

    plt.subplot(1, 2, 2)
    plt.ylabel('Gas padel/%')
    plt.xlabel('Time/s')
    plt.plot(tlist, ulist, color='000000')
    plt.legend
    plt.show()

def plotAni():
    plt.ion()
    plt.subplot(1, 2, 1)
    plt.ylabel('Velovity m/s')
    plt.xlabel('Time/s')
    plt.plot(tlist, vlist, label='Actual speed',color='000000')
    plt.plot(tlist, clist, label='Set speed', linestyle='--',color='000000')

    plt.subplot(1, 2, 2)
    plt.ylabel('Gas padel/%')
    plt.xlabel('Time/s')
    plt.plot(tlist, ulist,color='000000')
    plt.legend
    plt.pause(1/60)

aniflag = False
#Main program starts
if str(input('Key in y to draw animated graph: ')) == 'y':
    aniflag = True
else:
    if str(input) == '':
        aniflag = False

while t <= t_final:
    error = set_speed - v
    u = Kp * PControl(v) + Ki * IControl(I, error) + Kd * DControl(last_error, error)
    u = correct(u)
    v += dt * dvdt(u, v)
    vlist.append(v)
    ulist.append(u)
    elist.append(error)
    last_error = error
    t += dt
    tlist.append(t)
    clist.append(set_speed)
    if aniflag == True:
        plotAni()

plotNormal()