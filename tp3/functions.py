# Commande de génération de clé :
# openssl prime -generate -bits 512

from Cryptodome.Util.number import getPrime
# pip3 install pycryptodomex

# Questions 1.3 à 1.8...
def gen_rsa_keypair(bits):
  size = bits // 2 # (syntaxe '//' pour une division entière, sans resultat flottant)
  p = getPrime(size)
  q = getPrime(size)

  # Taille de la clé rsa = taille du module n 
  
  # quand on multiplie deux nombres :
  # -> la taille du resultat est la somme de la taille de ces 2 nombres.

  n = p * q                 # module de chiffrement
  phi_n = (p - 1) * (q - 1) # indicatrice d'Euler pour n

  # Question 4 :
  
  # Les multiples de phi_n sont (p-1) et (q-1).
  # Il faut vérifier que l'exposant n'est divisible ni par l'un ni par l'autre.
  
  e = 65537 # Exposant de chiffrement (ici un petit nombre premier standard)

  # Vérification des conditions nécessaires pour e (utile pour un exposant généré aléatoirement)
  assert(((p - 1) % e != 0) and ((q - 1) % e != 0))

  # Question 6

  # A l'aide de l'exposant e et de phi_n, on calcul l'inverse modulaire de e donc (e ** -1) % phi_n

  d = pow(e, -1, phi_n) # calcul l'inverse modulaire de e % phi_n

  return ((e, n), (d, n))


# Question 2.3
# -----
# Fonction qui fait l'exponentiation modulaire avec un entier m, et la paire (exposant e, module de chiffrement n)
# https://en.wikipedia.org/wiki/Modular_exponentiation
# -----
def rsa (m, e, n):
  return pow(m, e, n) 

# Chiffrement à l'aide du message à chiffrer m, d'une clé publique (e,n)
def rsa_enc (m, e, n):
  # Conversion d'une chaine encodée en utf-8 en bytes,
  # puis en entier à l'aide de la convention big endian.
  m_int = int.from_bytes(m.encode("utf-8"), 'big')

  # Le message m doit être strictement inférieur à n.
  if m_int >= n:
    raise ValueError("m must be lower to n.")
  
  return rsa(m_int, e, n)

# Déchiffrement à l'aide du chiffré c, d'une clé privée (d,n).
def rsa_dec (c, d, n):
  m_int = rsa(c, d, n)

  # conversion inverse d'un entier en chaine de caractère.
  m = m_int.to_bytes((m_int.bit_length() + 7) // 8, 'big').decode('utf-8')

  return m