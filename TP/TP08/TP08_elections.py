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

r = 0

r2 = 0

liste = []

if a > 0 and b > 0 :

while 1:

if a==b :

return a

elif a < b :

r = b % a

b = r

elif b < a :

r = a% b

a = r

if r == 0 :

return r2

r2 = r

elif a==0 and b == 0 : return 0





# Ligne suivante a decommenter pour tester

if __name__ == '__main__': testeur.fais_tests('01_pgcd')





# ***************************************************************************

# Crible d'Eratosthene

# ***************************************************************************



def eratosthene(n):

liste = [True] * (n+1)

comparateur = 2

liste[0]= False

liste[1]= False

#boucle qui enleve les mvs éléments

while comparateur < int(n**(0.5))+1 :

#On enleve les multiples de ce nmbr premier

if liste[comparateur-1] == True :

possible = n// liste[comparateur-1]

for i in range (possible) :

liste [i*liste[comparateur-1]] = False

#changement de comparateur

for i in range (comparateur , n+1 ) :

if liste[i]== True :

comparateur = i

result = []

for i in range (len(liste)):

if liste[i] == True :

result.append(i-1)

# Ligne suivante a decommenter pour tester

if __name__ == '__main__': testeur.fais_tests('02_eratosthene')





# ***************************************************************************

# Wall-Street !

# ***************************************************************************



def amplitude(cot):

return "Not good..."



# Ligne suivante a decommenter pour tester

#if __name__ == '__main__': testeur.fais_tests('03_amplitude')





def gain(cot):

return "Not good..."



# Ligne suivante a decommenter pour tester

#if __name__ == '__main__': testeur.fais_tests('04_gain')



def gain_date(cot):

return "Not good..."



# Ligne suivante a decommenter pour tester

#if __name__ == '__main__': testeur.fais_tests('05_gain_date')





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
