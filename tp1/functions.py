
import string
from collections import Counter

# Initialiser une liste contenant l'alphabet + caractères spéciaux.

# [ "A", "B" ..., "Z", " ", "'", "."]
decoder = list(string.ascii_uppercase) + [' ', '\'', '.']

# Initialiser un dictionnaire permettant d'encoder un msg.
encoder = { decoder[i]: i for i in range(len(decoder)) }

size = len(decoder)

def encode(msg):
  l = [ encoder[msg[c]] for c in range(len(msg))]
  return l

def decode(l):
  msg = [ decoder[l[i]] for i in range(len(l))]
  return "".join(msg)

# Question 2 :
def chiffre_cesar(msg, key):
  l = encode(msg)                   # Récupérer la liste de codes du message.
  l = [(n + key) % size for n in l] # Affecter le décalage de la clé k.
  return decode(l)                  # Retourner le chiffré sous forme de chaîne.

def dechiffre_cesar(cipher, key):
  inv_key = (size - key) % size         # Calculer la clé inverse de k.
  return chiffre_cesar(cipher, inv_key) # Chiffrer avec la clé inverse pour retrouvrer le message.

def plus_frequent(msg):
  # Stocker un dictionnaire avec les fréquences d'apparition de chaque caractère distint dans le msg
  frequencies = { c: msg.count(c) for c in set(msg) }

  # Renvoyer la clé du dictionnaire (caractère) dont la valeur (fréquence) est la plus élevée.
  key = max(frequencies, key = frequencies.get)
  return key

# Adaptation de la méthode plus_frequent pour permettre de
# retourner les caractères exaequo pour une fréquence max trouvée.
def plus_frequents(msg):
  # Stocker un dictionnaire avec les fréquences d'apparition de chaque caractère distint dans le msg.
  frequencies = Counter(msg)

  # Trouver la fréquence maximale parmi la liste de caractères.
  max_freq = frequencies[max(frequencies, key = frequencies.get)]

  # Sélectionner plusieurs caractères qui ont une même fréquence maximale.
  # Prendre toutes les clés qui ont une valeur max_freq
  r = list(filter(lambda c: frequencies[c] == max_freq, frequencies))

  return r

# Retrouver la clé à partir du caractère le plus fréquent d'un message chiffré.
def retreive_key_cesar(msg):
  c  = encoder[' ']                # caractère le plus courant encodé
  f  = encoder[plus_frequent(msg)] # caractères chiffré le plus fréquent encodé

  key = (f - c) % size
  return key

# Question 1.5

def chiffre_affine(msg, key):
  l = encode(msg)
  l = [(key[0] * n + key[1]) % size for n in l]
  return decode(l)

def dechiffre_affine(cipher, key):
   l = encode(cipher)
   l = [(n - key[1]) * pow(key[0], -1, size) % size for n in l]
   return decode(l)

# Question 1.7

def deux_plus_frequent(msg):
  frequencies = { c: msg.count(c) for c in set(msg) }

  l = sorted(frequencies, key = frequencies.get, reverse=True)[:2]
  return tuple(encoder[c] for c in l)

def retreive_key_affine(msg):
  y = deux_plus_frequent(msg)      # caractères chiffrés les plus fréquents
  x = (encoder[' '], encoder['E']) # caractères les plus courants

  a = ((y[0] - y[1]) * pow((x[0] - x[1]), -1, size)) % size
  b = (y[0] -  a * x[0]) % size
  return (a, b)

# Question 2.1

def chiffre_vigenere(msg, key):
  cipher = [ ((ord(msg[i]) - ord('A')) + (ord(key[i % len(key)]) - ord('A'))) % 26 + ord('A') for i in range(len(msg)) ]
  cipher = "".join([chr(n) for n in cipher])

  return cipher

def dechiffre_vigenere(cipher, key):
  inv_key = [ (26 - (ord(key[i]) - ord('A'))) + ord('A') for i in range(len(key))]
  inv_key = "".join([chr(n) for n in inv_key])

  msg = chiffre_vigenere(cipher, inv_key)
  return msg

# Question 2.2

# IC = probabilité que 2 lettres choisies aléatoirement dans un texte soient identiques.
# Permet d'en déduire la langue utilisée pour un chiffré.
def ic(cipher):
  n = len(cipher) # n : nombre de caractère dans le texte.
  sum = 0

  # Mi : le nombre d'apparition du i ème caractère dans le texte.
  # Calculer la somme total des expressions Mi * (Mi - 1) pour l'ensemble des caractères.
  
  # Boucler sur toutes les lettres de l'alphabet.
  for i in range(26):
    Mi = cipher.count(chr(i + ord('A')))
    sum += Mi * (Mi - 1)          
  
  ic = (1 / (n * (n - 1))) * sum  # ic = (Partie gauche de la relation) * (somme calculée précedemment)
  return round(ic, 5)

# Question 2.3
def calcul_longueur_cle(cipher):
  # Faire l'analyse de fréquence à l'aide de l'indice de coïncidence pour une longueur de clé probable allant de 3 à 10.

  # L'indice de coïncidence d'un message est identique à son chiffré avec un chiffrement de césar.
  # Cet indice change avec le décalage de vigenère, un même caractère peut-être chiffré en différents résultats.

  best = -1 # Stocke la longueur de clé liée à la meilleure distance.
  best_dist = 1

  for i in range(3, 11):
    # Découper le chiffré en n sous-chaîne en supposant que n est la longueur de clé.
    sous_chaines = get_sous_chaines(cipher, i)

    ics = [0 for _ in range(len(sous_chaines))]

    for k in range(len(sous_chaines)):
      ics[k] = ic(sous_chaines[k])

    # Calculer la moyenne des ic pour la longueur de clé i.
    ic_moyen = sum(ics) / len(ics)
    
    # Calculer la distance de la moyenne avec l'ic de l'alphabet français -> environ 0,0746
    dist = abs(0.0746 - ic_moyen)

    if best == -1 or dist < best_dist:
      best = i         # Longueur de clé actuelle
      best_dist = dist # Distance actuelle
  
  return best
  
def get_sous_chaines(cipher, n):
  sous_chaines = ['' for _ in range(n)]

  # Parcourir chaque caractère de cipher avec son index.
  for index, lettre in enumerate(cipher):
    # Ajouter la lettre à la sous-chaîne correspondante (index % n)
    sous_chaines[index % n] += lettre
  
  return sous_chaines

# Question 2.4
def calcul_decalage(sous_chaines): 
  keys_prob = [] # key_prob stockera pour chaque sous-chaine un tableau d'un ou n caractères.
  for c in sous_chaines:
    pfs = plus_frequents(c) # Renvoyer le ou les 2 caractères les plus fréquents de la sous chaine 
    decalage = [(chr((ord(pf) - ord('E')) % 26 + ord('A'))) for pf in pfs]
    keys_prob.append(decalage)
  return keys_prob

# Fonction récursive pour renvoyer les déchiffrés des combinaisons de clé possibles :
# Exemple à partir d'une clé [['M'], ['A', 'O'], ['Y'], ['H', 'L'], ['S', 'E']] :
# Tester les combinaisons de clés : mayhs mayhe mayls mayle moyhs moyhe moyls moyle
def get_prob_deciphers(cipher, key, prefix = '', deciphers = None):
  # Déclarer l'argument par défaut deciphers avec None et non {} car un dictionnaire est immuable !
  # Sinon une nouvelle liste est créée une fois lorsque la fonction est définie,
  # et la même liste est utilisée à chaque appel successif dans le programme.
  # cf: https://docs.python-guide.org/writing/gotchas/
  if deciphers == None: deciphers = {}

  if len(key) == 0:
    deciphers[prefix] = dechiffre_vigenere(cipher, prefix)
    return deciphers

  first = key[0]

  for c in first:
    # Appel récursif en retirant l'élement du tableau stocké dans first
    get_prob_deciphers(cipher, key[1:], prefix + c, deciphers)
  return deciphers

# Question 2.5
def attaque_vigenere(cipher):
  key_len = calcul_longueur_cle(cipher)

  print("key len :", key_len)

  sous_chaines = get_sous_chaines(cipher, key_len)

  # print("sous-chaine :", sous_chaines)

  decalages = calcul_decalage(sous_chaines)

  print("caractères constituant la clé probable :", decalages)

  return get_prob_deciphers(cipher, decalages)