
import string

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