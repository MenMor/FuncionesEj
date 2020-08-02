def Factorial(numero):
    nfact = 1
    for i in range(1, numero+1):
        nfact *= i
    return nfact

def PotenciaSumatoria(base, exponente):
    x=1
    for i in range(1, exponente+1):
        acum = 0
        for j in range(1, base+1):
            acum += x
        x = acum
    return acum


def SumatoriaCuadrado(numero):
    i=1
    acum=0
    while i <= (2*numero-1):
        acum += i
        i += 2
    return acum

def Potencia_Multiplicacion(base, exponente):
    acum = 1
    i = 1
    while i <= exponente:
        acum *= base
        i += 1
    return acum

def MetodoEuler(limite):
    sumatoria = 1
    for n in range(1, limite+1):
        num_factorial = (Factorial(n))
        num = (Potencia_Multiplicacion(2, n)) * (SumatoriaCuadrado(num_factorial))
        denominador = 2*n+1
        sumatoria += num/(Factorial(denominador))
    return sumatoria

def SumaDigitos(numero):
    suma=0
    while numero != 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma

def Primo (numero):
    cont = 0
    for i in (1, numero+1):
        if numero % i == 0:
            cont += 1
    if cont == 2:
        num_primo: bool = True
    else:
        num_primo: bool = False
    return num_primo


def Division_Resta(dividendo, divisor):
    x = 2
    respuesta = 0
    while x != 1:
        dividendo -= divisor
        respuesta += 1
        if dividendo < divisor:
            x = 1
            return respuesta




