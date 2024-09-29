from functions import *

# Question 1.1

# La paire de clé RSA contient une :
# - clé publique représentée par une paire (e, n) 
# - clé privée : (d, n)
# On retrouve dans les 2 paires le module de chiffrement RSA nommé n


# Question 1.2

# La taille des nombres premiers aléatoires p et q doit être égal à la moitié de la clé demandée, nommée 'bits'

print('----- Chiffrement / Déchiffrement RSA -----')
 
# Question 2.1

# (a) La clé publique (e,n) d'Alice doit être utilisée par Bob pour qu'il chiffre le message destiné à Alice.  
# (b) La clé privée (d,n) d'Alice doit être utilisée pour qu'elle puisse déchiffrer un message qui lui est destiné.


# Question 2.2

# En quelle opération consiste chacune des opérations a,b décrites précédemment ?

# (a) chiffré = (message) ** (exposant de chiffement e) % (module de chiffrement n)
# -> c = (m ** e) % n
# (b) message = (chiffré) ** (exposant de déchiffrement d) % (module de chiffrement n)
# -> m = (c ** d) % n

# Question 2.6 - Simuler un échange de message.entre Alice et Bob

rsa_kp_alice = gen_rsa_keypair(512)
rsa_kp_bob   = gen_rsa_keypair(512)

msg = 'J\'arrive dans une heure.'

print('Bob récupère la clé publique d\'Alice et lui chiffre un message...\n')
print('Bob :', msg)
public_key_alice = rsa_kp_alice[0]
cipher_bob = rsa_enc(msg, public_key_alice[0], public_key_alice[1])
print('Message chiffré de Bob :', cipher_bob, '\n')

print('Alice déchiffre le message de Bob avec sa clé privée...\n')

secret_key_alice = rsa_kp_alice[1]
decipher_bob = rsa_dec(cipher_bob, secret_key_alice[0], secret_key_alice[1])
print('Message dechiffré de Bob :', decipher_bob, '\n')

# Question 3.1

# (a) Bob doit utiliser sa clé privée pour signer un message.
# (b) Alice doit utiliser la clé publique de Bob pour vérifier l'authenticité du message qui prétend être signé par Bob.

# Question 3.2

# La procédure de signature est d'utiliser un algo de hachage pour hacher le message.
# Le hash obtenu est ensuite chiffré à l'aide de la clé privée, ce résultat représente la signature.

# La forme du message signé est donc (m, s) -> message chiffré, signature.

print('----- Chiffrement / Déchiffrement RSA avec signature -----')

msg = 'Le code d\'accès de la salle A152 est 1234 !'

print('Bob récupère la clé publique d\'Alice et lui chiffre un message.\n')
print('Bob :', msg)
public_key_alice = rsa_kp_alice[0]
cipher_bob = rsa_enc(msg, public_key_alice[0], public_key_alice[1])
print('Message chiffré de Bob :', cipher_bob, '\n')

secret_key_bob = rsa_kp_bob[1]
print('Bob signe son message à l\'aide de sa clé privée...\n')
signature_bob = rsa_sign(cipher_bob, secret_key_bob[0], secret_key_bob[1])

print('Signature du message de Bob :', signature_bob, '\n')

print('Alice vérifie la signature reçue à l\'aide de la clé publique de Bob...\n')

public_key_bob = rsa_kp_bob[0]

# Hash du chiffré de Bob. 
cipher_hash = h(cipher_bob)
# Résultat du déchiffrement de la signature à l'aide de la clé publique de Bob.
decipher_sign = rsa_verify(signature_bob, public_key_bob[0], public_key_bob[1])

print('Hash du chiffré :', cipher_hash)
print('Verification avec la clé publique de Bob :', decipher_sign)

if cipher_hash == decipher_sign:
  print('Signature vérifiée.\n')
else:
  print('Signature invalide.\n')

print('Alice déchiffre le message de Bob avec sa clé privée...\n')

secret_key_alice = rsa_kp_alice[1]
decipher_bob = rsa_dec(cipher_bob, secret_key_alice[0], secret_key_alice[1])
print('Message dechiffré de Bob :', decipher_bob, '\n')

# Question 4.1

# Il est possible, sans connaitre le message initial m de produire un chiffré c' à partir d'un chiffré c intercepté.
# Il suffira du multiplier c avec le chiffré d'un autre message quelquonque m':

# c′ = ( c × m′ ^ e) mod n

# Le destinataire, en déchiffrant c' obtiendra (m' x m) mod n
# Le message déchiffré sera le produit du message original m et du message m'

print('----- Test malléabilité -----')

rsa_kp_attaquant = gen_rsa_keypair(512)
public_key_attaquant = rsa_kp_attaquant[0]

m1 = 'Coucou Alice, c\'est Bob !'
c1 = rsa_enc(m1, public_key_alice[0], public_key_alice[1])

m2 = 'Pwet !'
c2 = rsa_enc(m2, public_key_attaquant[0], public_key_attaquant[1])

new_cipher = (c1 * (c2 ^ public_key_alice[0])) % public_key_alice[1]

# Déchiffrement par Alice
new_msg = rsa_dec(new_cipher, secret_key_alice[0], secret_key_alice[1])

# It doesn't works yet...
print('Message de Bob :', m1)
print('Autre Message :', m2)
print('Nouveau message produit :', new_msg)

# Question 4.2

# Le risque du problème de déterminisme et de permettre à un attaquant d'associer un chiffré répetitif à une donnée sensible comme un mot de passe.
# Il pourrait tente de retrouver le mot de passe chiffré à l'aide d'un dictionnaire.
# Le dictionnaire serait composé du mot de passe éventuels et de leur version chiffrée avec la clé publique interceptée.