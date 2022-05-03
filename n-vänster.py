import matplotlib.pyplot as plt
import numpy as np
import math

def drawFunc(t, function):
    y = np.array([None]*100) #f(t) kunde inte räknas ut som vektor automatiskt när f ingår i math eller Numpy.
    for i in range(0,100):
        y[i] = f(t[i]) #Detta gör en vektor av f(t)
        plt.plot(t,y)

def f(x):
    return x**2

def RiemannvänsterN(function, presicion, end): #Funktionen tar tre variabler, en funktion, prestionen på beräkningen samt ett slutvärde
    sum = 0
    for k in range (0,presicion): #från nott till presitionsvärdet beräknas nu summan av alla rektanglar
        sum += (end/presicion)*function(end*k/presicion)#varje rektangel ritas med breddet slutvärde/presition och hödjen slutvärdet*index/presition
    print ( sum ) #sumnan printas

def RiemanngrafikvänsterN(f, presicion, end): #funktionen tar samma variabler som i förra
    print(f(3))
    t = np.linspace(0, end, 100)
    drawFunc(t,f) #här ritas funktionen
    for i in range (0,presicion):
        x=np.array([i*end/presicion,i*end/presicion,(i+1)*end/presicion,(i+1)*end/presicion]) # för att ge korrekt bas på lådorna beräknas två pukter som basen går emellan och dessa läggs in som vektorer i x koordinaten
        y=np.array([0,f(i*end/presicion),f(i*end/presicion),0]) #samma sak händer här med y koordinaten nämnvärt är dock att funktionen här tar enbart i medans vi höger tar den i+1  och vid mitten ta den (2i+1)/2 se avancerad trapets flr resten
        plt.plot(x,y) #här plottas varje rektangel in
        plt.fill_between(x, y, facecolor='r', alpha=0.25)
    plt.title("Vänster") #titel
    plt.savefig("FunktionVänsterN.png") #här skrivs en bild ut av den ritade funktionen

RiemannvänsterN(f,10,1)
RiemanngrafikvänsterN(f,10,1)