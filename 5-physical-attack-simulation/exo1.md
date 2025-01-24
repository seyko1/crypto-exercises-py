# Exercice 1 - Simple Power Analysis

commande de test du programme :

> seselab test.asm /dev/null 

seselab attend un deuxième argument la sortie ou stocké la consomation :
- /dev/null si l'information ne nous interesse pas
- /dev/stdout pour afficher dans la sortie
- ou dans un fichier txt quelconque..

## Question 1.1

m = 286705839763 (message) 

N = 11972278303 (modulo)

s = 9402315191 (signature)

## Question 1.2

**modexp** fait l'exponentiation modulaire d'une valeur B à l'aide d'un exposant modulaire et d'une valeur de modulo


L'algorithme de **modexp** est celui vu en cours :
```
1 r := 1 // Résultat 
2 b := b % m
3 tant que e != 0:
4   si e & 1 = 1 alors:
5     r := (r * b) % m
6   fin
7   b := (b * b) % m
8   e := e >> 1
9 fin


e : exposant modulaire
B : valeur à élever à la puissance e modulo m
r : résultat qui évolue à chaque multiplication
```

Voici un petit exemple de l'évolution des valeurs pour l'expression `(10 ^ 10) % 19`

*(une ligne par opération)*

| m  	| e  	| b  	| r 	|
|----	|----	|----	|---	|
| 19 	| 10 	| 10 	| 1 	|
|    	|    	| 10 	|   	|
|    	|    	| 5  	|   	|
|    	| 5  	|    	|   	|
|    	|    	|    	| 5 	|
|    	|    	| 6  	|   	|
|    	| 2  	|    	|   	|
|    	|    	| 17 	|   	|
|    	| 1  	|    	|   	|
|    	|    	|    	| 9 	|
|    	|    	| 4  	|   	|
|    	| 0  	|    	|   	|

# Question 1.4

On constate dans un premier temps des baisses de consommation régulière dans le graphe de consommation.

Question 1.5

### a.

Ajout des instructions :
- dbg 220 lorsque r9 est pair.
- dbg 250 lorsque r9 est impair.

On constate le comportement suivant :

- Lorsque le bit de poid faible est impair :
  - grande ligne (dbg 250) + petite ligne (dbg 220)  
- lorsque le bit de poid faible est pair :
  - petite ligne (dbg 220)

(voir le fichier rsa-trace.png) 

### b.


En lisant de droite à gauche sur le graphe on retrouve la valeur binaire :

1 1 1 1 0 1 0 0 0 1 0 1 0 1 0 1 1 0 1 1 0 0 1 1 0 0 0 0 0 1

> echo "$((2#111101000101010110110011000001))" 

Valeur retrouvée : 1024814273

Correspondance binaire <-> hexa :
```
11'1101 0001'0101 0110'1100 1100'0001
3    D   1     5   6     C    C    1
```

L'exposant est égal à 1024814273

La valeur hexadécimale 3D156CC1 correspond bien à l'affectation faite aux ligne 26 à 29 dans `rsa.asm` pour définir l'exposant dans r3. 

