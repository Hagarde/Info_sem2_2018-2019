# Pour la lecture
import numpy as np
# Lecture des donnees
donnees_t,donnees_u = np.loadtxt('Uc_41.txt',unpack=True)

# Les trois derniers exercices vous permettent de determiner tout ce qu'il 
# faut pour calculer w0 et Q. En particulier, la pseudo-periode est reliee a 
# w0 et Q, ainsi que le temps caracteristique tau de decroissance: cherchez 
# dans vos cours de physique les relations adequates et inversez-les pour 
# trouver w0 et Q en fonction de T et tau.
 def periode(t,u,nb=10):
    liste_t = [] 
    for i in range(len(u)-1): 
        if u[i]*u[i+1] <= 0 and u[i+1]!=0: 
            liste_t.append(t[i]) 
        return (liste_t[nb] - liste_t[0]) * 2 / nb 
pseudo_periode = periode(donnees_t,donnees_u) 

 def temps_et_maxima(t,u): 
  liste_t = [] 
   liste_m = [] 
    for i in range(1,len(u)-1): #
        if u[i-1] < u[i] >= u[i+1]: 
            liste_t.append(t[i])
            liste_m.append(u[i]) 
    return  liste_t,liste_m 

 t_maxima,u_maxima = temps_et_maxima(donnees_t,donnees_u)
 i = 0 
 for value in u_maxima:
     if value < 0.05*u_maxima[0] :
         temps_caractéristique = t_maxima[i]
    i+=1
tout =pseudo_periode*temps_caractéristique 
tou = tout *tout 


Q  = (tout/4)+1
w0 = (2*Q) / temps_caractéristique
# Affichage des resultats demandes
print(w0,Q)
