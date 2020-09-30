import numpy as np

def sumatoria_reloj(matriz, posc_f, posc_c):
    suma = 0
    for i in range(posc_f - 1, posc_f + 1):
        for j in range(posc_c - 1, posc_c + 1):
            suma += matriz[i, j]
    return suma

matriz_alt = np.random.randint(1, 11, size=(10, 10))

# coordenadas fila, columna
fila_c = np.random.randint(10, size=(10, 1))
columna_c = np.random.randint(10, size=(10, 1))

sum_reloj = []
for i in range(0, len(fila_c)):
    posicion = int(fila_c[i])
    posicion_c = int(columna_c[i])
    sum_reloj.append(sumatoria_reloj(matriz_alt, posicion, posicion_c))

print(sum_reloj)
