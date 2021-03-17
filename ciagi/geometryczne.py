def wyraz_geo(a1, q, n):
    an = a1*(q**(n-1))
    return an

def suma_geo(a1, n, q):
    if q == 1:
        s = a1*n
    else:
        s = a1*(1-q**n)/(1-q)
    return s