# Basiswerte
from Crypto.Util.number import inverse
p = 13
q = 17
n = p * q
phi = (p - 1) * (q - 1)

# Schlüsselgenerierung
e = 11
d = inverse(e, phi)
print(f"Öffentlicher Schlüssel: ({e},{n})")
print(f"Privater Schlüssel: ({d},{n})")

# Nachricht
nachricht = int(input("Beliebige Zahl zwischen "
                      + "0 und 221 eintippen: "))

# Verschlüsseln
cypher = pow(nachricht, e, n)

# Entschlüsseln
print(pow(cypher, d, n))
