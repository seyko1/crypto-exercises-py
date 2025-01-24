import random

# Boîte de permutation
sbox = [0xc, 5, 6, 0xb, 9, 0, 0xa, 0xd, 3, 0xe, 0xf, 8, 4, 7, 1, 2]

# Sbox inversée (récupère l'index de chaque nombre de 0 à 14 !)
# L'index de la valeur 0 du tableau sbox est 5.
xobs = [sbox.index(i) for i in range(16)]

# Question 1.1
def round(m, k):
  return sbox[m ^ k] 
  # pour m = 1 et k = 2 :
  # 1 XOR 2 = 0001 XOR 0010 = 0011 = 3
  # sbox[3] = 11  

# Question 1.2
def enc(msg, key):
  r1 = round(msg, key[0])
  r2 = round(r1, key[1])
  return r2

# Question 1.3
def back_round(s, k):
  return xobs[s] ^ k

# Question 1.4
def dec(ctxt, key):
  r1 = back_round(ctxt, key[1])
  r2 = back_round(r1, key[0])
  return r2

# Question 2.1
def enc_bytes(msg, key):
  m1 = (msg >> 4) & 0xf # décaler puis ne garder que les 4 bits de poids faible
  m2 = msg & 0xf
  
  c1 = enc(m1, key)
  c2 = enc(m2, key)

  cipher = c1 << 4 | c2
  return cipher 

# Question 2.1
def dec_bytes(cipher, key):
    c1 = (cipher >> 4) & 0xf # bits de poids fort
    c2 = cipher & 0xf # bits de poids faible
  
    m1 = dec(c1, key)
    m2 = dec(c2, key)

    msg = m1 << 4 | m2
    return msg

# Question 2.4

def enc_file(file, key):
  with open(file, 'rb') as f:
    msg = f.read()

  enc_file_name = file.split('.')[0] + '.enc'
  
  bytes_cipher = bytes([enc_bytes(byte, key) for byte in msg])

  with open(enc_file_name, 'wb+') as enc_file:
    enc_file.write(bytes_cipher)

  return enc_file_name

# Question 2.5

def dec_file(file, key):
  with open(file, 'rb') as f:
    bytes_cipher = f.read()
  
  dec_file_name = file.split('.')[0] + '.dec'

  with open(dec_file_name, 'wb+') as dec_file:
    arr = [ dec_bytes(byte, key) for byte in bytes_cipher ]
    dec_file.write(bytes(arr))
  
  return dec_file_name

# Question 3.3 avec CBC

def enc_file_cbc(file, key, vector):
  with open(file, 'rb') as f:
    msg = f.read()

  enc_file_name = file.split('.')[0] + '.cbcenc'

  arr = []
  for c in msg:
    c = c ^ vector
    vector = enc_bytes(c, key)
    arr.append(vector)

  with open(enc_file_name, 'wb+') as enc_file:
    enc_file.write(bytes(arr))
  
  return enc_file_name

def dec_file_cbc(file, key, vector):
  with open(file, 'rb') as f:
    bytes_cipher = f.read()
  
  dec_file_name = file.split('.')[0] + '.cbcdec'

  # Le vecteur d'initialisation pour le premier tour sera le nombre pseudo-aléatoire utilisé pour le chiffrement.
  arr = []
  for byte in bytes_cipher:
    block_cipher_decryption = dec_bytes(byte, key)
    # déchiffré = octet déchiffré (avec la clé) XOR vecteur d'initialisation (1er tour) ou chiffré (tours suivants).
    plain_text = block_cipher_decryption ^ vector
    arr.append(plain_text)
    
    # le vecteur pour les prochains tours devient simplement l'octet chiffré
    vector = byte
  
  with open(dec_file_name, 'wb+') as dec_file:
    dec_file.write(bytes(arr))
  
  return dec_file_name