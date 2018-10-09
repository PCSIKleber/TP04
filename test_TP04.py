from test_TP04z import *

##################################
## Procédure d'exécution des tests
##################################

DICO = {'01_listes': ListesTest,
            '02_partie_entiere': PartieEntiereTest,
            '03_PE1':  PE1Test,
            '04_PE48': PE48Test,
            '05_fonction_Collatz': FCollatzTest,
            '06_orbite_Collatz': OrbiteCollatzTest,
            '07_tdv_Collatz': TempsDeVolCollatzTest,
            '08_altitude_Collatz': AltitudeCollatzTest,
            '09_ta_Collatz' : TACollatzTest,
            '10_tac_Collatz': TACCollatzTest,
            '11_plus_haut_Collatz': HautCollatzTest,
            '12_plus_long_Collatz': LongCollatzTest,
            '13_plus_long_en_altitude_Collatz': HautAltitudeCollatzTest,
            '14_plus_long_avant_la_chute_Collatz': HautChuteCollatzTest,
            }

def fais_tests(choix):
    '''Fonction qui appelle les batteries de test selon le choix de
    l'utilisateur.'''
    dico = DICO
    try:
        suite = unittest.TestLoader().loadTestsFromTestCase(dico[choix])
    except:
        print('='*70)
        print('Le choix "%s" ne fait pas partie des possibilites suivantes:' % choix)
        s = '\n  * '
        print(s[1:] + s.join(sorted(list(dico.keys()))))
        print('='*70)
        exit()
    unittest.TextTestRunner(verbosity=2).run(suite)


def calcule_note():
    '''Fonction qui calcule automatiquement la note de l'élève au prorata du
    nombre de tests passés avec succès.'''
    liste_testcases = ['test_TP04.' + elem.__name__ for elem in DICO.values()]
    suite = unittest.TestLoader().loadTestsFromNames(liste_testcases)
    f = open('erreurs.txt','w')
#    res = unittest.TextTestRunner(stream=f,verbosity=1).run(suite)
    res = unittest.TextTestRunner(verbosity=2).run(suite)
    f.close()
    f = open('erreurs.txt','r')
    explications = '''Resultats des tests: E = Error, F = Failure, . = Success'''
    s_ex = '\n' + '*'*len(explications) + '\n' + explications + '\n' + '*'*len(explications)
    print(s_ex)
    print(f.readline())
    f.close()
    total = res.testsRun
    failed= len(res.failures)
    errors= len(res.errors)
    success = total - failed - errors
    print("Vous avez reussi {} tests sur un total de {}.".format(success,total))
    print("Note indicative: {}/20 (sans compter la penalite 'commentaires')".format(int(success/total*20)))

##################################
# Calcul de la note du TP
##################################

def detaille_note():
    '''Pour calculer les notes à chaque sous-suite de tests.'''
    total_general  = 0
    success_general= 0
    for k in sorted(DICO.keys()):
        s = unittest.TestLoader().loadTestsFromTestCase(DICO[k])
        f = open('erreurs.txt','w')
        res = unittest.TextTestRunner(stream=f,verbosity=1).run(s)
        f.close()
        total = res.testsRun
        failed= len(res.failures)
        errors= len(res.errors)
        success = total - failed - errors
        print("{}/{}".format(success,total),k)
        total_general += total
        success_general += success
    print('='*20)
    print('Globalement: {}/{}'.format(success_general,total_general))
    print('Note indicative: {}/20'.format(round(success_general/total_general*20,2)))
