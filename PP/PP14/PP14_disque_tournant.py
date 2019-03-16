# Import de Numpy qui sert a lire le fichier
import numpy as np
# Lecture du fichier
t,u = np.loadtxt('inertie_p_PP.txt',unpack=True,skiprows=1)

# A vous de jouer en mettant dans la variable omega300 la valeur de la vitesse 
# angulaire lors du 300e passage par un trou et dans theta10 la valeur de 
# l'angle au plus proche de t=10s

signal_montant = (max(u) + min(u)) /2#valeur à partir de laquelle ondetect le signal 
duree = t[-1] - t[0]#duree entrze deux signaux 
temps = [] #liste des moment au dessus valeur limite s
#determination des moments ou il y a signal montant 
for i in range(len(u) ): 
    if u[i] > signal_montant : 
        temps.append(t[i])


compteur = 0
for j in range (len (temps)-1) :
    if temps [j+1] -temps [j] > duree*50:   
        compteur +=1



def theta (t) :
    derivee = (np.pi /6) /(temps[2]-temps [1])
    return derivee *t
def omega (t) :
    a =theta (temps[2]) -theta(temps[1])
    return (a / (temps[2]-temps[1]))*t
    
    
    
    
    
omega300 = omega(t[300])
theta10  = theta(10)


# A la fin, on affiche les resultats a l'ecran
print(omega300,theta10)
