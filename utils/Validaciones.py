def es_matriz_cuadrada(A):
    n = len(A)
    return all(len(fila) == n for fila in A)


def tiene_diagonal_valida(A):
    n = len(A)
    for i in range(n):
        if A[i][i] == 0:
            return False
    return True


def es_diagonal_dominante(A):
    n = len(A)
    for i in range(n):
        suma = sum(abs(A[i][j]) for j in range(n) if j != i)
        if abs(A[i][i]) < suma:
            return False
    return True


def es_matriz_3x3(A):
    return len(A) == 3 and all(len(fila) == 3 for fila in A)


def listas_mismo_tamano(x_vals, y_vals):
    return len(x_vals) == len(y_vals)


def valores_x_unicos(x_vals):
    return len(set(x_vals)) == len(x_vals)
