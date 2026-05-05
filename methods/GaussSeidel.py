from utils.Validaciones import (
    es_matriz_3x3,
    tiene_diagonal_valida,
    es_diagonal_dominante
)


def GaussSeidel(A, b, x0=None, tol=1e-6, max_iter=100):

    if not es_matriz_3x3(A):
        raise ValueError("La matriz A debe ser 3x3")

    if len(b) != 3:
        raise ValueError("El vector b debe ser de tamaño 3")

    if x0 is not None and len(x0) != 3:
        raise ValueError("x0 debe ser de tamaño 3")

    if not tiene_diagonal_valida(A):
        raise ValueError("La matriz tiene ceros en la diagonal")

    if not es_diagonal_dominante(A):
        print("Advertencia: puede no converger")

    n = 3
    x = x0[:] if x0 else [0.0, 0.0, 0.0]
    error = float("inf")  # ✅ CORRECCIÓN: inicializar antes del loop

    for k in range(max_iter):
        x_old = x[:]

        for i in range(n):
            suma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - suma) / A[i][i]

        error = max(abs(x[i] - x_old[i]) for i in range(n))

        if error < tol:
            return {
                "solucion": x,
                "iteraciones": k + 1,
                "error": error,
                "converge": True
            }

    return {
        "solucion": x,
        "iteraciones": max_iter,
        "error": error,
        "converge": False
    }
