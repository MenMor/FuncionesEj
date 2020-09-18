# Ejemplo funcion recursiva sin retorno
def cuenta_regresiva(numero):
   numero -= 1
   if numero > 0:
       print(numero)
       cuenta_regresiva(numero)
   else:
       print("Fin")
       print(numero)

print(cuenta_regresiva(5))


# Funcion recursiva con retorno
def get_factorial(numero):
    if numero == 0:
        return 1
    return numero * get_factorial(numero-1)

print(get_factorial(5))


def get_potencia(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a * get_potencia(a, b-1)

print(get_potencia(2, 4))


