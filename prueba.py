import numpy as np

matriz_A = np.random.randint(11, size=(10, 10))
print(matriz_A)

# matriz transpuesta
matriz_T = np.ones((10, 10))
for i in range(0, len(matriz_A)):
    for j in range(0, len(matriz_A[i])):
        matriz_T[j, i] = matriz_A[i, j]
print("\n", matriz_T)

for i in range(0, len(matriz_T)):
    for j in range(0, len(matriz_T[i])):
        if i == j:
            matriz_T[i, j] = 0
print("\n", matriz_T)
