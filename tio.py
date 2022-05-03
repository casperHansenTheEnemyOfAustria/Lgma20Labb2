import matplotlib.pyplot as plt
import numpy as np

def f(x):
    y = x**2
    return y


def RiemannTio(function):
    sum = 0 
    for k in range (0,10):
        sum += (1/10)*function(k/10)
    print ( sum )

def RiemanngrafikTio(f):
    print(f(3))
    t = np.linspace(0, 1, 100)
    plt.plot(t,f(t))
    for i in range (0,10):
        x=np.array([i/10,i/10,(i+1)/10,(i+1)/10])
        y=np.array([0,f(i/10),f(i/10),0])
        plt.plot(x,y)
        plt.fill_between(x, y, facecolor='r', alpha=0.25)
    plt.title("V-rsum presition 10")
    plt.savefig("Funktion.png")

RiemannTio(f)
RiemanngrafikTio(f)