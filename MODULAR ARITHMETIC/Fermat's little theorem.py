"""
Fermat's little theorem
states that if p is a prime number, 
then for any integer a, the number (a^p - a) is an integer multiple of p. In the notation of modular arithmetic, 
this is expressed as
 -> a^p = a (mod p)
 """

print(pow(3,17)%17)

"""
If a is not divisible by p, 
that is, if a is coprime to p, then Fermat's little theorem is equivalent to the statement that
 a^(p - 1) - 1 is an integer multiple of p

 -> a^(p-1) = 1 (mod p)
"""

print(pow(2,6)%7) # a must by not divisinle by p 

"""
to find Modular_multiplicative_inverse a^-1 is not equal to 1/a 

in anthor we we have to use fermant's little theorm 

by using it 

a^(p-1)=1 mod p # *a-1
so a^(p-2) = a^-1 mod p
than a^-1 = a^(p-2) mod p
"""
# What is the inverse element: 3 * d ≡ 1 mod 13?
a= 3
p =13
d = pow(a,p-2) % p
print(d,f"!= 1/{a}")

