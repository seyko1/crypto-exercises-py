from functions import *

# Création d'un crypto-système jouet, un réseau de substitution à 2 tours
# Utilisation d'une permutation triviale / identité.

# Le principe de permutation consiste à faire passer des bits qui ont été influencés par une boite s
# dans un endroit ou ils vont être influencés par une autre boite p

# L'étape de permutation n'existe pas ici car on en a qu'une seule,
# Elle prend 4 bits en entrée et fournit 4 bits en sortie

# On utilisera la boîte S de PRESENT vu en cours

# -------------------------------------------------

# Question 1.5 (tester l'égalité)

print('----- Chiffrement avec un nibble [0, 15] -----')

msg = 1
key = (7, 8)

cipher = enc(msg, key)
print('Message :', msg)
print('Clé :', key)
print('Chiffré :', cipher)

decipher = dec(cipher, key)
print('Déchiffré :', decipher)

# Question 2.2

print('\n')
print('----- Chiffrement avec un octet -----')

msg = 137

cipher = enc_bytes(msg, key)
print('Message :', msg)
print('Clé :', key)
print('Chiffré :', cipher)

decipher = dec_bytes(cipher, key)
print("Déchiffré :", decipher)

# Question 2.3

print('\n')
print('----- Chiffrement avec caractère ascii -----')

msg = 'M'

cipher = enc_bytes(ord(msg), key)
print('Message :', msg)
print('Clé :', key)
print('Chiffré :', cipher)

decipher = dec_bytes(cipher, key)
print("Déchiffré :", chr(decipher))

# Question 2.4

print('\n')
print('----- Chiffrement d\'un fichier -----')

file = 'files/pwet.txt'
print('Fichier à chiffrer :', file)
enc_file_name = enc_file(file, key)
print('Message chiffré dans :', enc_file_name)

# Question 2.5

dec_file_name = dec_file(enc_file_name, key)
print('Message déchiffré dans :', dec_file_name)

print('\n')
print('----- Chiffrement du fichier test.txt avec la clé (9,0) -----')

key = (9, 0)
file = 'files/test.txt'
print('Fichier à chiffrer :', file)
enc_file_name = enc_file(file, key)
print('Message chiffré dans :', enc_file_name, '👽️')
# output : boYboY1/1boYboY1;

# Question 3.1
# On constate qu'une partie du chiffré est le même pour une partie du message en clair "coucou".

# Question 3.2

# Une attaque possible serait de capturer et réutiliser des blocs de message chiffré répétitif pour tenter de manipuler le texte brut déchiffré.
# Ce bloc rejoué pourrait représentée une donnée sensible.
# Une analyse de fréquence comme pour vigenere pourrait également être utilisée par un attaquant pour en déduire le texte en clair.

print('\n')
print('----- Chiffrement du fichier test.txt avec CBC -----')

print('Fichier à chiffrer :', file)

# vecteur d'initialisation qui servira au chiffrement et au déchiffrement
init_vector = random.randint(0, 255)

enc_file_name = enc_file_cbc(file, key, init_vector)
print('Message chiffré dans :', enc_file_name, '👽️')

print('Fichier à déchiffrer :', enc_file_name)
dec_file_name = dec_file_cbc(enc_file_name, key, init_vector)
print('Message déchiffré dans :', dec_file_name, '👽️')

# Question 3.4

# Le chiffré du message test.txt ne contient plus de répétition lorsqu'il est chiffré dans le mode CBC.
# L’avantage de la génération aléatoire du vecteur d’initialisation est de rendre le message unique
# et de corriger les vulnérabilités du mode ECB utilisé précedemment.