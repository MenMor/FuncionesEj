import numpy as np
def get_factorial(numero):
    return np.prod(np.arange(2, numero+1))

valor = float(input("Ingrese valor para calcular factorial: "))
print(f"{valor}! = {get_factorial(valor)}")


def get_matriz_aleatiria(filas, columnas):
    return np.random.randint(1, 10, (filas, columnas))


def get_matriz_a (matriz):
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
        suma_c = np.sum([i[j] ** 3 for i in matriz])
        suma_c = suma_c ** (1 / 3)
        w = np.append(w, suma_c)

    sum = 0
    for i in range(0, len(w)):
        for j in range(0, len(vt[i])):
            mult = w[i] * vt[i]
            sum += mult

    s_form = 1 / sum
    s = np.ones((4, 4))
    s = s.astype(float)
    for i in range(0, len(s)):
        for j in range(0, len(s[i])):
            s[i, j] = s_form

    return s

matriz_1 = np.array([[1, 2, 3, 4],
                    [3, 4, 5, 6],
                    [5, 6, 7, 8],
                    [7, 8, 9, 10]])

matriz_s = get_matriz_a(matriz_1)
print(matriz_s)
