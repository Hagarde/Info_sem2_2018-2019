# ***************************************************************************
# Ceci est le squelette du fichier dans lequel *toutes* vos fonctions doivent

# etre ecrites. Il a ete quelque peu adapte pour vous permettre d'executer des

# tests automatiquement et sans effort: il suffira de decommenter la ligne if

# #if __name__ == '__main__': testeur.fais_tests('...')

# presente apres chaque definition de fonction.

#

# ***ATTENTION*** Pour que cela fonctionne bien dans pyzo, il est

# ***absolument primordial*** de lancer l'execution dans le menu via

# "Executer en tant que script" ou "Run file as script"

# c'est-a-dire avec le raccourci Ctrl-Shift-E (et NON simplement Ctrl-E) sinon

# les mises a jour de votre fichier ne seront pas prises en compte.

# (NB: Si vous etes sous Mac, c'est Pomme-Shift-E qu'il faut utiliser)

# ***************************************************************************





# On importe la batterie de tests uniquement a l'execution du fichier et non

# lors de l'import en tant que module:

if __name__ == '__main__': import test_TP08 as testeur





# ***************************************************************************

# Determination du PGCD par algorithme d'Euclide

# ***************************************************************************



def pgcd(a,b):
    r0 = a
    r1=b 

    r3 = 1
    if a == 0 or b == 0 : return 0
    while r3 != 0 : 
        result = r3           
        r3 =  max(r0,r1) % min(r1,r0)
        r0 =min(r1,r0)
        r1 = r3 

    return result 
    
    
    
    
    



# Ligne suivante a decommenter pour tester

if __name__ == '__main__': testeur.fais_tests('01_pgcd')





# ***************************************************************************

# Crible d'Eratosthene

# ***************************************************************************



def eratosthene(n):
    if n == 0 or n == 1 : return []
    
    liste = [True] * (n+1)
    
    comparateur = 1
    
    liste[0]= False
    
    liste[1]= False

    while comparateur < int(n**(0.5))+1 :
        comparateur +=1
        if liste [comparateur ] == True : 
            limite = n // comparateur 
            for k in range (2,limite+1) :
                liste [comparateur * k ] = False 
            
    result = []
    for l in range (len(liste)) :
        if liste[l] == True : result.append(l)
    return result 
    
# Ligne suivante a decommenter pour tester

if __name__ == '__main__': testeur.fais_tests('02_eratosthene')


# ***************************************************************************

# Wall-Street !

# ***************************************************************************



def amplitude(cot):
    max  = cot[0]
    min  = cot[0]
    for prix in cot :
        if prix < min : min = prix 
        if prix > max : max = prix 

    return abs(max - min )



# Ligne suivante a decommenter pour tester

if __name__ == '__main__': testeur.fais_tests('03_amplitude')





def gain(cot):
    liste = []
    for i in range (len(cot)) :
        for j in range (i) : 
            liste.append(cot[i]-cot[j])
    maxi = liste[0]
    for gain in liste :
        if gain > maxi : maxi = gain 
        
    return maxi



# Ligne suivante a decommenter pour tester

if __name__ == '__main__': testeur.fais_tests('04_gain')



def gain_date(cot):
    liste = []
    maxi = 0 
    t= 0 
    for i in range (len(cot)) :
        for j in range (i) : 
            a =  cot[i]-cot[j]
            liste.append(a)
            temps = abs (i - j)
            if a > maxi : 
                maxi = a 
                t = temps
            elif a == maxi : 
                if t >  temps : t = temps 
            
    return maxi , t 

# Ligne suivante a decommenter pour tester

if __name__ == '__main__': testeur.fais_tests('05_gain_date')





def gain1(cot):

    return "Not good..."



# Ligne suivante a decommenter pour tester

#if __name__ == '__main__': testeur.fais_tests('06_gain1')



def gain1_date(cot):

    return "Not good..."



# Ligne suivante a decommenter pour tester

#if __name__ == '__main__': testeur.fais_tests('07_gain1_date')





# ***************************************************************************

# Le jeu electoral

# ***************************************************************************



def winner(vote,k):

    return "Not good..."



# Ligne suivante a decommenter pour tester

#if __name__ == '__main__': testeur.fais_tests('08_winner')



def gagnant_tour1(vote):

    return "Not good..."



# Ligne suivante a decommenter pour tester

#if __name__ == '__main__': testeur.fais_tests('09_tour1')



def gagnant_tour1_bis(vote):

    return "Not good..."



# Ligne suivante a decommenter pour tester

#if __name__ == '__main__': testeur.fais_tests('10_tour1_bis')



def gagnant_tour2(vote):

    return "Not good..."



# Ligne suivante a decommenter pour tester

#if __name__ == '__main__': testeur.fais_tests('11_tour2')



def gagnant_tour2_bis(vote):

    return "Not good..."



# Ligne suivante a decommenter pour tester

#if __name__ == '__main__': testeur.fais_tests('12_tour2_bis')







# Calcul de la note finale

if __name__ == '__main__': testeur.detaille_note()
