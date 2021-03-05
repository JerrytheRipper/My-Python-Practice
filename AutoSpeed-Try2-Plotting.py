import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


#Assign physic quantities
set_speed = 25
u = 0.00
v = 0.00
t = 0.00
dt = 0.01
m = 700
k = 0.5 * 0.24 * 1.225 * 5
Fp = 3000
#Assign variables
ulist=[]
vlist=[]
tlist=[]

#Define functions
def dudt(v):
    #if set_speed - v > 0:
    #    return (set_speed - v)**2
    #if set_speed - v < 0:
    #    return -(set_speed - v)**2
    return 6*(set_speed-v)**3
def dvdt(u, v):
    return (Fp * u - k * (v ** 2)) / m
def correct(u):
    if u > 1.00:
        u = 1.00
    if u < -0.50:
        u = -0.50
    return u
#Define plotting function


#Main program starts
while t <= 60:
    v += dvdt(u ,v) * dt
    u += dudt(v) *dt
    u = correct(u)
    vlist.append(v)
    ulist.append(u)
    t += dt
    tlist.append(t)


#class matplotlib.animation.FuncAnimation(fig, func, frames=None, init_func=None, fargs=None, save_count=None, *, cache_frame_data=True, **kwargs)
plt.ylabel('Velovity m/s')
plt.xlabel('Time s')
plt.plot(tlist,vlist)
plt.show()