num_capicua = int(input("Ingrese número: "))

def get_lista_numero(numero):
    lista = []
    i = 4
    while i == 4:
        ultimo = numero % 10
        lista.append(ultimo)
        numero //= 10
        if numero == 0:
            i = 7
    lista.reverse()
    return lista

print(get_lista_numero(num_capicua))

def get_lista_numero_invertido(numero):
    num_invertido = []
    i = 4
    while i == 4:
        ultimo = numero % 10
        num_invertido.append(ultimo)
        numero //= 10
        if numero == 0:
            i = 7
    return num_invertido

print(get_lista_numero_invertido(num_capicua))

def capicua(list_1, list_2):
    long = len(list_1)
    i = 0
    while i < long:
        if list_1[i] == list_2[i]:
            i += 1
            if i == long:
                return True
        else:
            return False

if capicua(get_lista_numero(num_capicua), get_lista_numero_invertido(num_capicua)):
    print("Es capicua")
else:
    print("No es capicua")

