def NewtonRaphson2x2(f, g, df_dx, df_dy, dg_dx, dg_dy,
                     x0, y0, tol=1e-6, max_iter=100):

    x, y = x0, y0
    error = float("inf")  # ✅ CORRECCIÓN: inicializar antes del loop

    for k in range(max_iter):

        try:
            F = [f(x, y), g(x, y)]
        except Exception:
            raise ValueError(
                "Error al evaluar las funciones en el punto actual"
            )

        try:
            J = [
                [df_dx(x, y), df_dy(x, y)],
                [dg_dx(x, y), dg_dy(x, y)]
            ]
        except Exception:
            raise ValueError(
                "Error al evaluar las derivadas en el punto actual"
            )

        det = J[0][0] * J[1][1] - J[0][1] * J[1][0]

        if abs(det) < 1e-14:  # ✅ CORRECCIÓN: comparar con tolerancia, no con 0
            return {
                "solucion": (x, y),
                "iteraciones": k,
                "error": error,
                "converge": False,
                "mensaje": "Jacobiano singular (det ≈ 0)"
            }

        delta_x = (-F[0] * J[1][1] + J[0][1] * F[1]) / det
        delta_y = (-J[0][0] * F[1] + F[0] * J[1][0]) / det

        x += delta_x
        y += delta_y

        error = max(abs(delta_x), abs(delta_y))

        if error < tol:
            return {
                "solucion": (x, y),
                "iteraciones": k + 1,
                "error": error,
                "converge": True
            }

    return {
        "solucion": (x, y),
        "iteraciones": max_iter,
        "error": error,
        "converge": False,
        "mensaje": "No convergió en el número máximo de iteraciones"
    }
