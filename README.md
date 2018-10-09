TP04 Poursuite de l'échauffement
================================

Ce fichier permet de rappeler les choses à faire sans fioritures. Pour plus de détails et d'indications sur la syntaxe, voir la version pdf et celle qu'on vous aura distribué en cours.

Mise en jambe
-------------

NB: si vous écrivez les listes à suivre « à la main », vous n’aurez aucun point...

1.  Créer la liste `L1` constituée de 12 zéros.

2.  Créer la liste `L2 = [42,41,40,39,...,26,25,24]` (il s’agit de remplir les `...` de manière automatisée.

3.  Créer la liste `L3 = [0,0,0,2,2,2,4,4,4,...,10,10,10]`

4.  Créer la liste `L4 = [1,2,2,3,3,3,...,7,7,7,7,7,7,7,...,10,10]`. Stocker son 40-ième élément dans la variable `L4_40`.

5.  Créer la liste `L5 = [1, 2,1, 3,2,1, 4,3,2,1, ..., 9,8,7,6,5,4,3,2,1]`. Stocker son 38-ième élément dans la variable `L5_38`.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


6. Partie entière: Implémenter la fonction `partie_entiere(x)` pour laquelle vous avez préparé un algorithme à la maison.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.

7. ProjectEuler numéro 1:   Écrire la fonction `probleme_1()` sans argument qui renvoie la somme de tous les entiers multiples de 3 _ou_ de 5 qui soient strictement inférieurs à 1000.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


8. ProjectEuler numéro 48:  Écrire la fonction `probleme_48()` sans argument qui renvoie le nombre constitué des 10 derniers chiffres de la somme des i puissance i avec i variant de 1 à 1000.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


Conjecture de Collatz
---------------------

1.  Implémenter la fonction `f(n)` de Collatz qui divise n par 2 s'il est pair et le multiplie par 3 et rajoute 1 sinon. Stocker dans la variable `trente_premiers` la liste `[f(1), f(2), f(3), ..., f(29), f(30)]` (calculée de manière automatique, cela va sans dire...).

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


2.  Écrire le programme qui prend `orbite(n)` qui prend comme entrée l’entier `n` et qui renvoie son orbite sous forme d’une liste. Stocker dans la variable `orbite_de_27` l’orbite de 27.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


3.  Écrire une fonction `temps_de_vol(a)` qui renvoie le temps de vol (nombre total d'entiers visités sur l'orbite) correspondant à l’orbite de `a`.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


4.  Écrire une fonction `altitude(a)` qui renvoie l’altitude (plus grand entier visité sur l'orbite) de l’orbite de `a`. Pour s’entraîner, on implémentera la recherche du maximum « à la main ».

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


5.  Écrire une fonction `temps_en_altitude(a)` qui renvoie le temps de vol en altitude (nombre d'étapes avant de passer strictement en dessous du nombre de départ) correspondant à l’orbite de `a`. On prendra comme convention que ce temps vaut 1 si `a` vaut initialement $1$.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


6.  Écrire une fonction `temps_avant_chute(a)` qui renvoie le temps de vol avant la chute (nombre d'étapes minimum après lequel on ne repasse plus au-dessus de la valeur de départ) pour l’orbite de `a`. À nouveau, on prend comme convention qu’il vaut 1 si `a` vaut initialement 1.

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


À présent que l’on dispose de ces outils, utilisons-les pour faire un
peu de (variante autour du ProjectEuler numéro 14).

7.  Pour des entiers de départ de valeur strictement inférieures à un
    million, déterminer à chaque fois

    1.  celui qui monte le plus haut en altitude et la valeur de cette altitude maximale (à stocker dans la liste `le_plus_haut` qui aura donc deux éléments `[a,altitude(a)]`).

    2.  celui dont le temps de vol est le plus long et la valeur de ce
        temps de vol (à stocker dans la liste `le_plus_long`).

    3.  celui dont le temps de vol en altitude est le plus long et la
        valeur de ce temps de vol (à stocker dans la liste `le_plus_long_en_altitude`).

    4.  celui dont le temps de vol avant la chute est le plus long et la
        valeur de ce temps de vol (à stocker dans la liste `le_plus_long_avant_la_chute`).

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.


8.  Ne trouvez-vous pas que la procédure suggérée fasse un peu « gâchis » ?
    Implémentez une procédure unifiée qui puisse effectuer tous les calculs précédents en moins de temps (en sacrifiant peut-être un peu sur l’autel de la simplicité de conception). Estimez le gain de temps que l’on peut espérer et mesurez-le (via un `import time` et à l’aide de `time.clock()`, plus d’info avec `help(time.clock)`). N’oubliez pas de tester votre procédure en retrouvant les résultats précédent

**STOP GITHUB**: Allez sur Github Desktop pour faire un commit. Choisissez vous-même (avec pertinence) le résumé. Pensez aussi à appuyer sur le bouton «Push origin» en haut à droite pour mettre à jour sur le serveur web.
