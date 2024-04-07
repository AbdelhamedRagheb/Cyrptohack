def is_quadratic_residue(n,p):
    if n % p == 0 :
        return True
    return pow(n,(p-1)//2,p) == 1

def tonelli_shanks(n,p):
    Roots=[]
    if n % p ==0 :
        return 0
    
    if not is_quadratic_residue(n,p):
        print("This value of n is not quadratic residue.")
        return None
    else:
        print("This value of n is quadratic residue.")
    
    if p % 4  == 3 :
        return pow(n,(p+1)//4,p)
    
    Q =p -1
    S = 0
    while Q % 2 == 0 :
        S+=1
        Q //= 2
    print("Q=",Q)
    print("S=",S)

    z = 2
    while is_quadratic_residue(z,p):
        z +=1 
    print("z=",z)

    M = S
    c = pow(z ,Q,p)
    t = pow(n, Q, p)
    R = pow(n,(Q+1)//2,p)

    print("M=",M)
    print("c=",c)
    print("t=",t)
    print("R=",R)

    while t != 1:
        print("Loop")
        i = 0
        temp = t 
        while temp != 1:
            i +=1
            temp = (temp*temp)%p
        print("i=",i)

        pow2 = 2**(M - i - 1)
        b = pow(c,pow2,p)
        M = i 
        c = (b*b)%p
        t = (t * b* b) % p
        R = (R*b)%p

        print("b=",b)
        print("M=",M)
        print("c=",c)
        print("t=",t)
        print("R=",R)
        Roots.append(R)


    return Roots
# r^2 = 5 mod 41
p = 30531851861994333252675935111487950694414332763909083514133769861350960895076504687261369815735742549428789138300843082086550059082835141454526618160634109969195486322015775943030060449557090064811940139431735209185996454739163555910726493597222646855506445602953689527405362207926990442391705014604777038685880527537489845359101552442292804398472642356609304810680731556542002301547846635101455995732584071355903010856718680732337369128498655255277003643669031694516851390505923416710601212618443109844041514942401969629158975457079026906304328749039997262960301209158175920051890620947063936347307238412281568760161
a = 8479994658316772151941616510097127087554541274812435112009425778595495359700244470400642403747058566807127814165396640215844192327900454116257979487432016769329970767046735091249898678088061634796559556704959846424131820416048436501387617211770124292793308079214153179977624440438616958575058361193975686620046439877308339989295604537867493683872778843921771307305602776398786978353866231661453376056771972069776398999013769588936194859344941268223184197231368887060609212875507518936172060702209557124430477137421847130682601666968691651447236917018634902407704797328509461854842432015009878011354022108661461024768

print(min(tonelli_shanks(a,p)))