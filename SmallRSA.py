# RSA kodieren und dekodieren
from Crypto.Util.number import inverse

# Basiswerte
p = 13
q = 17
n = p * q
phi = (p - 1) * (q - 1)

# Schlüsselgenerierung
e = 11
d = inverse(e, phi)
print("Privater Schlüssel: ({:d},{:d})".format(e, n))
print("Öffentlicher Schlüssel: ({:d},{:d})".format(d, n))

# Nachricht
nachricht = int(input("Beliebige Zahl zwischen 0 und 221 eintippen: "))

# Verschlüsseln
c = pow(nachricht, e, n)
print("Verschlüsselt: " + str(c))

# Entschlüsseln
m = pow(c, d, n)
print("Entschlüsselt: " + str(m))
