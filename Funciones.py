import numpy as np
def Factorial(numero):
    nfact = 1
    for i in range(1, numero+1):
        nfact *= i
    return nfact

def get_factorial(numero):
    if numero == 0:
        return 1
    return numero * get_factorial(numero-1)


def PotenciaSumatoria(base, exponente):
    x = 1
    acum = 0
    for i in range(1, exponente+1):
        acum = 0
        for j in range(1, base+1):
            acum += x
        x = acum
    return acum

def Potencia_Multiplicacion(base, exponente):
    acum = 1
    i = 1
    while i <= exponente:
        acum *= base
        i += 1
    return acum

def get_potencia_recursiva(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a * get_potencia_recursiva(a, b-1)


def SumatoriaCuadrado(numero):
    i = 1
    acum = 0
    while i <= (2*numero-1):
        acum += i
        i += 2
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
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma


def Division_Resta(dividendo, divisor):
    x = 2
    respuesta = 0
    while x != 1:
        dividendo -= divisor
        respuesta += 1
        if dividendo < divisor:
            x = 1
            return respuesta


def primo_compuesto(numero):
    iteracion_mitad = int((numero ** (1 / 2)) // 1)
    cont = 0
    for i in range(1, iteracion_mitad + 1):
        if numero % i == 0:
            cont += 1
    if cont == 1:
        return True
    else:
        return False

def get_list_primos(numero):
    lista = []
    cont = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            cont += 1
            lista.append(i)
    return lista

print("\nNumero primo o compuesto y sus valores divisibles:")
num = int(input("Ingrese número: "))
if primo_compuesto(num):
    print(f"{num} Es Primo. \n Valores divisibles: {get_list_primos(num)}")
else:
    print(f"{num} Es compuesto. \n Valores divisibles: {get_list_primos(num)}")


def promedio(lista):
    suma = np.sum(lista)
    promedio = suma / len(lista)
    return promedio


