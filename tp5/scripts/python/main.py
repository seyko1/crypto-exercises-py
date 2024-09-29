from Cryptodome.Util.number import getPrime
import math
import random

# Question 2.1

size = 512

p = getPrime(size)
q = getPrime(size)

while p == q: q = getPrime(size)

n = p * q

e = 65537

phi_n = (p - 1) * (q - 1)

assert((math.gcd(e, p-1) == 1) and (math.gcd(e, q-1) == 1))

d = pow(e, -1, phi_n)

m = random.randint(0, 1000)
print(m)