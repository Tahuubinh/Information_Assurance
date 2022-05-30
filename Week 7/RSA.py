p = 5701
q = 5743
e = 8959    # 17 * 17 * 31

n = p * q
phi_n = (p - 1) * (q - 1)

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
   
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def keyGen(p, q, e):
    phi_n = (p - 1) * (q - 1)
    return findModInverse(e, phi_n)

def binToDec(M):
    MDec = 0
    exponent = 1
    for i in range(len - 1, -1, -1):
        MDec += M[i] * exponent
        exponent *= 2
    return exponent

d = keyGen(p, q, e)

M = {1,1,0,0,1,0,1,0,1,0,1,0,0,1,1,1}
len_M = len(M)




