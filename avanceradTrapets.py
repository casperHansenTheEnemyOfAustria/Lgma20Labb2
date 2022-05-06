import matplotlib.pyplot as plt
import numpy as np
import math

def drawFunc(t, function):
    y = np.array([None]*100) #f(t) kunde inte räknas ut som vektor automatiskt när f ingår i math eller Numpy.
    for i in range(0,100):
        y[i] = f(t[i]) #Detta gör en vektor av f(t)
        plt.plot(t,y)

def f(x):
    return 1/(math.sqrt(2*math.pi))* math.exp(-x*x/2)


def trapetsN(function, presicion, end): #Definiera en funktion av 0 variabler, som räknar
    sum = 0 #summan av rektanglars area (bredd 1/10, höjd f(x))
    for k in range (0,presicion): #från noll till presitionsvärdet beräknas nu summan av alla rektanglar
        sum += (end/presicion)*(function(end*k/presicion)+function(end*(k+1)/presicion))/2 #varje rektangel ritas med breddet slutvärde/presition och hödjen slutvärde*(f(a)+f(b))/2/presition
    return ( sum ) #sumnan returneras


def trapetsgrafikN(f, presicion, end): #Funktionen tar tre variabler, en funktion, prestionen på beräkningen samt ett slutvärde
    t = np.linspace(0, end, 100)
    drawFunc(t,f) #Här ritas den faktiska funktionen
    for i in range (0,presicion):
        #i i detta fallet ger placering typ första rektangeln osv
        x=np.array([i*end/presicion,i*end/presicion,(i+1)*end/presicion,(i+1)*end/presicion]) # för att ge korrekt bas på lådorna beräknas två pukter som basen går emellan och dessa läggs in som vektorer i x koordinaten
        yValue = (f(i*end/presicion)+f((i+1)*end/presicion))/2 #denligt dry principen beräknas trapetsmetodens y-värde här och sätts till en variabel
        y=np.array([0,yValue,yValue,0]) #samma sak händer här med y koordinaten nämnvärt är dock att funktionen här använder sig av trapetsmetoden vilket gör att yvärdet istället beräknas med slutvärde*(f(a)+f(b))/2/presition
        plt.plot(x,y)
        plt.fill_between(x, y, facecolor='r', alpha=0.25)
    plt.title("Trapets")
    plt.savefig("FunktionAvanceradTrapetsN.png")


i=0.67448
# trapetsN(f,10000,500)/2
while 0.25 > trapetsN(f,10000,i): #här loopas trapetsfunktionen igenom fr att se när den träffar värdet på 1/2 av en halvan av just denn funktionen
    i+=0.000000001
    print(i)
# trapetsgrafikN(f,50,10)
print ("svaret är " + str(i))