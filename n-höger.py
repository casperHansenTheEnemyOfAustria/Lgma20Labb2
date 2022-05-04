import matplotlib.pyplot as plt
import numpy as np
import math

def drawFunc(t, function):
    y = np.array([None]*100) #f(t) kunde inte räknas ut som vektor automatiskt när f ingår i math eller Numpy.
    for i in range(0,100):
        y[i] = f(t[i]) #Detta gör en vektor av f(t)
        plt.plot(t,y)

def f(x):
    return math.sin(30*x)


def RiemannhögerN(function, presicion, end): #Definiera en funktion av 0 variabler, som räknar
    sum = 0 #summan av rektanglars area (bredd 1/10, höjd f(x))
    print(presicion)
    for k in range (0,presicion):
        sum += (end/presicion)*function(end*(k+1)/presicion)
    print ( sum )

def RiemanngrafikhögerN(f, presicion, end):
    print(f(3))
    t = np.linspace(0, end, 100)
    drawFunc(t,f)
    for i in range (0,presicion):
        x=np.array([i*end/presicion,i*end/presicion,(i+1)*end/presicion,(i+1)*end/presicion])
        y=np.array([0,f((i+1)*end/presicion),f((i+1)*end/presicion),0])
        plt.plot(x,y)
        plt.fill_between(x, y, facecolor='r', alpha=0.25)
    plt.title("Höger")
    plt.savefig("FunktionNHöger.png")

RiemannhögerN(f,10000,1)
RiemanngrafikhögerN(f,10000,1)