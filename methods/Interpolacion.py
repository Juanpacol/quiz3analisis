from utils.Validaciones import listas_mismo_tamano, valores_x_unicos


def InterpolacionLagrange(x_vals, y_vals, x_eval):

    # ✅ CORRECCIÓN: validaciones que faltaban
    if not listas_mismo_tamano(x_vals, y_vals):
        raise ValueError("x_vals e y_vals deben tener el mismo tamaño")

    if len(x_vals) < 2:
        raise ValueError("Se necesitan al menos 2 puntos para interpolar")

    if not valores_x_unicos(x_vals):
        raise ValueError("Los valores de x deben ser únicos (no repetidos)")

    n = len(x_vals)
    resultado = 0.0

    for i in range(n):
        termino = y_vals[i]

        for j in range(n):
            if j != i:
                termino *= (x_eval - x_vals[j]) / (x_vals[i] - x_vals[j])

        resultado += termino

    return resultado
