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

print('Bob récupère la clé publique d\'Alice et lui chiffre un message.')
print('Bob :', msg)
public_key_alice = rsa_kp_alice[0]
cipher_bob = rsa_enc(msg, public_key_alice[0], public_key_alice[1])
print('Message chiffré de Bob :', cipher_bob, '\n')

print('Alice déchiffre le message de Bob avec sa clé privée.')

secret_key_alice = rsa_kp_alice[1]
decipher_bob = rsa_dec(cipher_bob, secret_key_alice[0], secret_key_alice[1])
print('Message dechiffré de Bob :', decipher_bob, '\n')

