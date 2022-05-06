import matplotlib.pyplot as plt
import numpy as np

def f(x):
    y = x**2
    return y


def RiemannHundra(function): #Definiera en funktion av 0 variabler, som räknar
    sum = 0 #summan av rektanglars area (bredd 1/10, höjd f(x))
    for k in range (0,100):
        sum += (1/100)*function(k/100)
    print ( sum )

def RiemanngrafikHundra(f):
    print(f(3))
    t = np.linspace(0, 1, 1000)
    plt.plot(t,f(t))
    for i in range (0,100):
        x=np.array([i/100,i/100,(i+1)/100,(i+1)/100])
        y=np.array([0,f(i/100),f(i/100),0])
        plt.plot(x,y)
        plt.fill_between(x, y, facecolor='r', alpha=0.25)
    plt.title("V-rsum presition 100")
    plt.savefig("Funktion100.png")

RiemannHundra(f)
RiemanngrafikHundra(f)