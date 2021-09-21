import math
import mpmath
pi = 3.14159265358979323
e = 2.71828182845904523
gamma = 0.57721566490153286
def floor(v):
    m = int(v)
    return(m)
def ceiling(v):
    m = int(v)
    if m == v:
        return(m)
    if (m < v < m+1):
        return(m+1)
def abs(v):
    if v == 0:
        return("0")
    elif v > 0:
        return(v)
    elif v < 0:
        return(0-v)
def prime(v):
    m = floor(v)
    k = ceiling(v)
    for n in range(2, m):
        if m % n == 0:
            return(m, "is composite")
        if not (m % n == 0):
            return(m, "is prime")
    for a in range(2, k):
        if k % a == 0:
            return(k, "is compostite")
        if not (k % a == 0):
            return(k, "is prime")
    if v == 1:
        return("1 is neither prime nor composite")
    if v == 2:
        return("2 is the only even prime number")    
    if v == 0:
        return("whole numbers only please")
    if v < (m+0.5):
        return(prime(m))
    if ((m+0.5) <= v <= k):
        return(prime(k))
def W(v):
    return(mpmath.lambertw(v))
def rad(p, b):
    return(b**(1/p))
def ln(p):
    return(math.log(p))
def log(p):
    return(math.log(p)/math.log(10))
def basedlog(b, p):
    return(math.log(p)/math.log(b))
def sin(theta):
    return(math.sin(theta))
def sinh(theta):
    return(math.sinh(theta))
def arcsin(theta):
    return(math.arcsin(theta))
def arcsinh(theta):
    return(math.arcsinh(theta))
def cos(theta):
    return(math.cos(theta))
def cosh(theta):
    return(math.cosh(theta))
def arccos(theta):
    return(math.arccos(theta))
def arccosh(theta):
    return(math.arccosh(theta))
def tan(theta):
    return(math.tan(theta))
def tanh(theta):
    return(math.tanh(theta))
def arctan(theta):
    return(math.arctan(theta))
def arctanh(theta):
    return(math.arctanh(theta))
def csc(theta):
    return(mpmath.csc(theta))
def csch(theta):
    return(mpmath.csch(theta))
def arccsc(theta):
    return(mpmath.arccsc(theta))
def arccsch(theta):
    return(mpmath.arccsch(theta))
def sec(theta):
    return(mpmath.sec(theta))
def sech(theta):
    return(mpmath.sech(theta))
def arcsec(theta):
    return(mpmath.arcsec(theta))
def arcsech(theta):
    return(mpmath.arcsech(theta))
def cot(theta):
    return(mpmath.cot(theta))
def coth(theta):
    return(mpmath.coth(theta))
def arccot(theta):
    return(mpmath.arccot(theta))
def arccoth(theta):
    return(mpmath.arccoth(theta))