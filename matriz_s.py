import numpy as np

matriz = np.array([[1, 2, 3, 4],
                    [3, 4, 5, 6],
                    [5, 6, 7, 8],
                    [7, 8, 9, 10]])

v = []
for i in range(len(matriz)):
    suma = np.sum(matriz[i] ** 2)
    raiz = suma ** (1 / 2)
    raiz = round(raiz, 2)
    v = np.append(v, raiz)

vt = np.array([[1], [1], [1], [1]])
vt = vt.astype(float)
for i in range(0, len(v)):
    for j in range(0, len(v)):
        vt[i] = v[i]

w = []
for j in range(len(matriz)):
    suma_c = np.sum([i[j] ** 3 for i in matriz])  # Creo una lista compuesta para crear w con valores de cada columna
    suma_c = suma_c ** (1 / 3)
    w = np.append(w, suma_c)

sum = 0
for i in range(0, len(w)):
    for j in range(0, len(vt[i])):
        mult = w[i] * vt[i]
        sum += mult

s_form = 1 / sum  # 1 / sum * sum
s = np.ones((4, 4))
s = s.astype(float)
for i in range(0, len(s)):
    for j in range(0, len(s[i])):
        s[i, j] = s_form

print(s)



"""   v = np.zeros(1, 6)
    w = np.zeros(1, 6)
    vt = np.zeros(6, 1)
    for i in range(len(matriz)):
        v[0, i] = np.round(np.sum(matriz[i, :]**2)**(1/2), 2)

    for i in range(len(matriz)):
        w[0, i] = np.round(np.sum(matriz[:, i]**2)**(1/3), 2)

    for j in range(len(matriz)):
        vt[j, 0] = v[0, j]"""