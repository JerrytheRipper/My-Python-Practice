import matplotlib.pyplot as plt
import numpy as np

#simulate y^2=3x^3+2x^2+4, in range 0 to 100, with step 0.1 on x-axis
#create y list
ylist = []
#initialise all input values
x = float(0)
x1 = float(0)
y = float(4)
y1 = float(0)
dx = float(0.1)
k = float(0)
k1= float(0)
#define functions
def func(x):
    return (3*x**3 + 2*x**2 +4)**0.5

def increment_x(x):
    x1 = x + dx
    return x1

def increment_y(y,k):
    y1 = y + dx * k
    return y1

def last_k(x,y):
    return ((3 * x ** 3 + 2 * x ** 2 + 4) / (2 * y))

def new_k(x1,y1):
    return ((3 * x ** 3 + 2 * x ** 2 + 4) / (2 * y))

k = new_k(x , y)
ylist.append(y)
#loop
for n in range(1,1000):
    y1=increment_y(y,k)
    x1=increment_x(x)
    ylist.append(y1)
    k = new_k(x1 , y1)
    y=y1
    x=x1
    n+=1

xplot = np.arange(0 , 100 , 0.1)
yplot = np.array(ylist)
plt.figure()
plt.plot(xplot, func(xplot) , color = 'red' , linestyle = '--')
plt.plot(xplot , yplot)
plt.show()