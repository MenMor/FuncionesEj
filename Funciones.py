def Factorial (numero):
    nfact = 1
    for i in range(1,numero+1):
        nfact *= i
    return nfact

def PotenciaSumatoria(Base, Exponente):
    x=1
    for i in range(1,Exponente+1):
        acum = 0
        for j in range(1, Base+1):
            acum += x
        x = acum
    return acum


def SumatoriaCuadrado (numero):
    i=1
    acum=0
    while i <= (2*numero-1):
        acum += i
        i += 2
    return acum

def Potencia_Multiplicacion(Base, Exponente):
    acum = 1
    i = 1
    while i <= Exponente:
        acum *= Base
        i += 1
    return acum

def MetodoEuler (Limite):
    S=1
    for n in range(1, Limite+1):
        nf = (Factorial(n))
        num = (Potencia_Multiplicacion(2,n)) * (SumatoriaCuadrado(nf))
        D = 2*n+1
        S += num/(Factorial(D))
    return S

def SumaDigitos (numero):
    suma=0
    while numero != 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma

def Primo (numero):
    cont = 0
    for i in (1,numero+1):
        if numero % i == 0:
            cont += 1
    if cont == 2:
        Nprimo: bool = True
    else:
        Nprimo: bool = False
    return Nprimo


def Division_Resta( Dividendo, Divisor ):
    x = 2
    R = 0
    while x != 1:
        Dividendo -= Divisor
        R += 1
        if Dividendo < Divisor:
            Resultado = R
            x = 1
    return Resultado


