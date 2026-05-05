from utils.Validaciones import es_matriz_3x3


def LU(A, b):
    """
    Resuelve el sistema Ax = b usando descomposición LU con pivoteo parcial.
    
    Args:
        A: Matriz de coeficientes 3x3
        b: Vector de términos independientes (tamaño 3)
    
    Returns:
        dict con solución, iteraciones (0), error y converge
    """
    if not es_matriz_3x3(A):
        raise ValueError("La matriz A debe ser 3x3")
    
    if len(b) != 3:
        raise ValueError("El vector b debe ser de tamaño 3")
    
    n = 3
    
    # Crear copias para no modificar las originales
    A = [fila[:] for fila in A]
    b = b[:]
    
    # Matrices L y P (identidades iniciales)
    L = [[0.0] * n for _ in range(n)]
    P = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    
    # Descomposición LU con pivoteo parcial
    for k in range(n):
        # Encontrar el pivote máximo en la columna k
        max_val = abs(A[k][k])
        max_row = k
        for i in range(k + 1, n):
            if abs(A[i][k]) > max_val:
                max_val = abs(A[i][k])
                max_row = i
        
        # Intercambiar filas en A, b, P y L
        A[k], A[max_row] = A[max_row], A[k]
        b[k], b[max_row] = b[max_row], b[k]
        P[k], P[max_row] = P[max_row], P[k]
        
        for j in range(k):
            L[k][j], L[max_row][j] = L[max_row][j], L[k][j]
        
        # Si el pivote es cero, la matriz es singular
        if abs(A[k][k]) < 1e-10:
            raise ValueError("La matriz es singular o casi singular")
        
        # Calcular multiplicadores y actualizar fila
        for i in range(k + 1, n):
            L[i][k] = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] = A[i][j] - L[i][k] * A[k][j]
    
    # A partir de aquí, A es la matriz U
    U = A
    
    # Resolver Ly = Pb (forward substitution)
    y = [0.0] * n
    for i in range(n):
        suma = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - suma) / 1.0  # L[i][i] = 1
    
    # Resolver Ux = y (backward substitution)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        suma = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - suma) / U[i][i]
    
    # Calcular error (residual)
    residual = 0.0
    for i in range(n):
        suma = sum(U[i][j] * x[j] for j in range(n))
        residual = max(residual, abs(suma - b[i]))
    
    return {
        "solucion": x,
        "iteraciones": 0,
        "error": residual,
        "converge": residual < 1e-6
    }
