from functions import *

print('\n')
print('-----Chiffrement de césar sur un alphabet personnalisé -----')
print('\n')

# Question 1.1

message = 'HELLO WORLD.'
array   = encode(message)

print('Message :', message)
print('Caractères encodés :', array)
print('Message décodé :', decode(array))

# Question 1.2

key = 3
cipher = chiffre_cesar(message, key)
print('Chiffré :', cipher)

decipher = dechiffre_cesar(cipher, key)
print('Déchiffré :', decipher)

# Question 1.3

print ('Caractère le plus fréquent dans', message, '->', plus_frequent(message))

# Question 1.4

print('\n')
print('----- Déchiffrement du fichier enc_cesar.txt -----')
print('\n')

f = open('assets/enc_cesar.txt')
enc_cesar = f.read()
f.close()

c = plus_frequent(enc_cesar)
print('Caratère le plus fréquent du fichier :', c)
# output : A

# On considérera que le caractère 'A' chiffré correspond au caractère ' ' qui est le plus fréquent.

# 29 : modulo.
# 0  : plus fréquent chiffré.
# 26 : plus courant de l'alphabet actuel.

# y             = (x + key) % 29
# 0             = (26 + key) % 29
# (0 - 26) % 29 = key

key = retreive_key_cesar(enc_cesar)
print('Clé du chiffré enc_cesar.txt :\n', key)

dec_cesar = dechiffre_cesar(enc_cesar, key)

print('Message déchiffré de en_cesar.txt :', dec_cesar)

# Question 1.5 / 1.6

print('\n')
print('----- Chiffrement & déchiffrement affine du mot INFORMATIQUE-----')
print('\n')

# clé
key_affine = (13, 12)
print('Clé :', key_affine)

msg_affine = 'INFORMATIQUE'
print('Message :', msg_affine)

cipher_affine = chiffre_affine(msg_affine, key_affine)
print('Chiffré :', cipher_affine)

decipher_affine = dechiffre_affine(cipher_affine, key_affine)
print('Déchiffré :', decipher_affine)

# Question 1.8

print('\n')
print('----- Retrouver la clé à 2 inconnues du chiffrement affine -----')
print('\n')

f = open('assets/enc_affine.txt')
enc_affine = f.read()
f.close()

print('Chiffré de enc_affine.txt :', enc_affine, '\n')

enc_affine_key = retreive_key_affine(enc_affine)
print('Clé de enc_affine.txt :', enc_affine_key, '\n')

dec_affine = dechiffre_affine(enc_affine, enc_affine_key)

print('Déchiffré de enc_affine.txt :', dec_affine)

print('\n')
print('----- Chiffrement de vigenere -----')
print('\n')

key_vigenere = 'PWET'
msg_vigenere = 'JEREPRENDSDESCOURSENTROISIEMEANNEEDELICENCEETLECOURSDEPABLOESTTROPCHOUETTE'

# Question 2.1

print('-- Exemple avec clé --')
print('Message à chiffré :', msg_vigenere)
print('Clé :', key_vigenere)

cipher_vigenere = chiffre_vigenere(msg_vigenere, key_vigenere)

print('Chiffré :', cipher_vigenere)

print('Déchiffré :', dechiffre_vigenere(cipher_vigenere, key_vigenere), '\n')


print('-- Attaque de vigenère sans clé --')

f = open('assets/file2_enc.txt')
enc2 = f.read()
f.close()

print("Attaque file2_enc.txt 👽️\n", attaque_vigenere(enc2), '\n')

# --------------------

f = open('assets/file3_enc.txt')
enc3 = f.read()
f.close()

print("Attaque file3_enc.txt 👽️\n", attaque_vigenere(enc3), '\n')

# --------------------

f = open('assets/file4_enc.txt')
enc4 = f.read()
f.close()

fichier = open("assets/file4_dec.txt", "w+")
fichier.truncate(0)

fichier.write(str(attaque_vigenere(enc4)))
fichier.close()
print("Attaque file4_enc.txt 👽️\n -> Ouvrir le fichier file4_dec.txt 👽️\n")