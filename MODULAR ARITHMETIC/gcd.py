# Euclidean algorithm (GCD)
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    

# Extended Euclidean algorithm (EGCD)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

print(egcd(66528,52920 ))
print(gcd(66528 ,52920))
