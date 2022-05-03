import matplotlib.pyplot as plt
import numpy as np
import math
#se avancerad trapets för resten av förklaringen
def drawFunc(t, function):
    y = np.array([None]*100) #f(t) kunde inte räknas ut som vektor automatiskt när f ingår i math eller Numpy.
    for i in range(0,100):
        y[i] = f(t[i]) #Detta gör en vektor av f(t)
        plt.plot(t,y)

def f(x):
    return x**2


def trapetsN(function, presicion, end): #Definiera en funktion av 0 variabler, som räknar
    sum = 0 #summan av rektanglars area (bredd 1/10, höjd f(x))
    print(presicion)
    for k in range (0,presicion):
        sum += (end/presicion)*(function(end*k/presicion)+function(end*(k+1)/presicion))/2
        print(sum)
    print ( sum )

def trapetsgrafikN(f, presicion, end):
    print(f(3))
    t = np.linspace(0, end, 100)
    drawfunc(t,f)
    for i in range (0,presicion):
        x=np.array([i*end/presicion,i*end/presicion,(i+1)*end/presicion,(i+1)*end/presicion])
        y-value = (f(i*end/presicion)+f((i+1)*end/presicion))/2 #denligt dry principen beräknas trapetsmetodens y-värde här och sätts till en variabel
        y=np.array([0,y-value,y-value,0])
        plt.plot(x,y)
        plt.fill_between(x, y, facecolor='r', alpha=0.25)
    plt.title("Trapets")
    plt.savefig("FunktionTrapetsN.png")

trapetsN(f,10,1)
trapetsgrafikN(f,10,1)