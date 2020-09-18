import numpy as np

#Ejercicio 2
matriz_A = np.random.randint(11, size=(10, 10))
print(matriz_A)

# matriz transpuesta
matriz_T = np.ones((10, 10))
for i in range(0, len(matriz_A)):
    for j in range(0, len(matriz_A[i])):
        matriz_T[j, i] = matriz_A[i, j]
print("\n", matriz_T)

# Diagonal principal con 0
for i in range(0, len(matriz_T)):
    for j in range(0, len(matriz_T[i])):
        if i == j:
            matriz_T[i, j] = 0
print("\n", matriz_T)



# Ejercicio 1
matriz_B = np.random.randint(11, size=(10, 10))
print('\n\n', matriz_B)

r1 = np.arange(1, 11).reshape(10, 1)

r = []
cont = 0
x = 1
while x <= 10:
    cont = 0
    for i in range(0, len(matriz_B)):
        for j in range(0, len(matriz_B[i])):
            if matriz_B[i, j] == x:
                cont += 1
    r.append(cont)
    x += 1

r1 = np.insert(r1, 1, r, axis=1)
print(r1)

