# the square root modulo 
# a^2 = x mod p
# x  = a^2 mod p 
a = 5 # a^2
p = 29 
roots =[]
for i in range(29):
    if a == (pow(i,2)%p) :
        roots.append(i)
print(roots) #print the roots of a^2 
# but this way not the right way in high p 
