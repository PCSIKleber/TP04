# ***************************************************************************
# Ceci est le squelette du fichier dans lequel *toutes* vos fonctions doivent
# etre ecrites. Il a ete quelque peu adapte pour vous permettre d'executer des
# tests automatiquement et sans effort: il suffira de decommenter la ligne if
# if __name__ == '__main__': testeur.fais_tests('...')
# presente apres chaque definition de fonction.
#
# ***ATTENTION*** Pour que cela fonctionne bien dans pyzo, il est
# ***absolument primordial*** de lancer l'execution dans le menu via
# "Executer  en tant que script" ou "Run file as script"
# c'est-a-dire avec le raccourci Ctrl-Shift-E (et NON simplement Ctrl-E) sinon
# les mises a jour de votre fichier ne seront pas prises en compte.
# (NB: Si vous etes sous Mac, c'est Pomme-Shift-E qu'il faut utiliser)
# ***************************************************************************


# On importe la batterie de tests uniquement a l'execution du fichier et non
# lors de l'import en tant que module:
if __name__ == '__main__': import test_TP04 as testeur 


# ***************************************************************************
# Quelques listes a definir simplement
# ***************************************************************************

L1 = [1,1,1,'Caramba !']
L2 = [1,1,1,'Caramba !']
L3 = [1,1,1,'Caramba !']
L4 = [1,1,1,'Caramba !']
L5 = [1,1,1,'Caramba !']

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('01_listes')



# ***************************************************************************
# Implementation de la partie entiere
# ***************************************************************************

def partie_entiere(x):
    '''docstring a remplir....'''
    return []

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('02_partie_entiere')



# ***************************************************************************
# Project Euler numeros 1 et 48
# ***************************************************************************

def probleme_1():
    '''docstring a remplir....'''
    return []

def probleme_48():
    '''docstring a remplir....'''
    return []

# Lignes suivantes a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('03_PE1')
#if __name__ == '__main__': testeur.fais_tests('04_PE48')



# ***************************************************************************
# Le gros morceau: la conjecture de Collatz
# ***************************************************************************

def f(n):
    '''docstring a remplir....'''
    return []

trente_premiers = [1,1,1,1,"Caramba !"]

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('05_fonction_Collatz')

def orbite(a):
    '''docstring a remplir....'''
    return []

orbite_de_27 = [1,1,1,1,"Caramba !"]

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('06_orbite_Collatz')

def temps_de_vol(a):
    '''docstring a remplir....'''
    return []

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('07_tdv_Collatz')

def altitude(a):
    '''docstring a remplir....'''
    return []

# Ligne suivante a decommenter pour tester
#if __name__ == '__main__': testeur.fais_tests('08_altitude_Collatz')


# Et pour la suite, vous avez compris le principe...


# Ligne suivante a decommenter pour tester le temps en altitude
#if __name__ == '__main__': testeur.fais_tests('09_ta_Collatz')


## Pour la fin, je vous donne la possibilite de ne pas faire tous les calculs
## deux fois avec la structure suivante


# Variable a passer a False avant de rendre votre TP
faire_les_calculs = True

# Initialisations dans lesquelles vous pourrez mettre les valeurs "en dur" en
# me laissant le code  correct apres pour que je puisse y jeter un oeil.
le_plus_haut = [3,174]  # Exemple non contractuel


# Pour eviter l'execution en double
if __name__ == '__main__' and faire_les_calculs:
    # Mettre ici le bloc d'instructions permettant le calcul effectif.



    print(le_plus_haut) # Pour que vous puissiez noter la valeur apres calcul



# Ligne suivante a decommenter pour tester le temps avant la chute
#if __name__ == '__main__': testeur.fais_tests('10_tac_Collatz')

# Ligne suivante a decommenter pour tester le plus haut
#if __name__ == '__main__': testeur.fais_tests('11_plus_haut_Collatz')

# Ligne suivante a decommenter pour tester le plus long
#if __name__ == '__main__': testeur.fais_tests('12_plus_long_Collatz')

# Ligne suivante a decommenter pour tester le plus haut en altitude
#if __name__ == '__main__': testeur.fais_tests('13_plus_long_en_altitude_Collatz')


# Ligne suivante a decommenter pour tester le plus haut avant la chute
#if __name__ == '__main__': testeur.fais_tests('14_plus_long_avant_la_chute_Collatz')


# Calcul de la note finale
if __name__ == '__main__': testeur.detaille_note()
