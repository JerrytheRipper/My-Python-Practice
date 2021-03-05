#Assign physic quantities
set_speed = 25
u = 0.00
v = 0.00
t = 0.00
dt = 0.10
m = 700
k = 0.5 * 0.24 * 1.225 * 5
Fp = 3000
#Assign variables
ulist=[]
vlist=[]
tlist=[]

def dudt(v):
    if set_speed - v > 0:
        return (set_speed - v)**2
    if set_speed - v < 0:
        return -(set_speed - v)**2
def dvdt(u, v):
    return (Fp * u - k * (v ** 2)) / m
def correct(u):
    if u > 1.00:
        u = 1.00
    if u < -0.50:
        u = -0.50
    return u

while t <= 10:
    v += dvdt(u ,v) * dt
    u += dudt(v) *dt
    u = correct(u)
    vlist.append(v)
    ulist.append(u)
    t += dt
    tlist.append(t)

    #testprint
    print(ulist)
    print(vlist)
    print(tlist)