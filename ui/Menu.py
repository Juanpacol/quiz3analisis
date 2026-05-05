import os
import sys

# Permite importar desde las subcarpetas del proyecto
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

import streamlit as st  # noqa: E402

from methods.GaussSeidel import GaussSeidel  # noqa: E402
from methods.Interpolacion import InterpolacionLagrange  # noqa: E402
from methods.Jacobi import Jacobi  # noqa: E402
from methods.NewtonRaphson import NewtonRaphson2x2  # noqa: E402
from methods.SOR import SOR  # noqa: E402
from utils.Validaciones import (  # noqa: E402
    es_diagonal_dominante,
    tiene_diagonal_valida,
)

st.set_page_config(page_title="Métodos Numéricos", layout="centered")
st.title("Métodos Numéricos")


# ──────────────────────────────────────────
# UI helpers
# ──────────────────────────────────────────

def input_matriz(prefix, defaults=None):
    d = defaults or [[4, 1, 1], [2, 5, 1], [1, 1, 4]]
    st.markdown("**Matriz A**")
    A = []
    for i in range(3):
        cols = st.columns(3)
        fila = []
        for j in range(3):
            v = cols[j].number_input(
                f"a{i+1}{j+1}",
                value=float(d[i][j]),
                key=f"{prefix}_a{i}{j}",
                label_visibility="collapsed",
            )
            fila.append(v)
        A.append(fila)
    return A


def input_b(prefix, defaults=None):
    d = defaults or [7.0, 11.0, 7.0]
    st.markdown("**Vector b**")
    cols = st.columns(3)
    return [
        cols[i].number_input(
            f"b{i+1}",
            value=d[i],
            key=f"{prefix}_b{i}",
            label_visibility="collapsed",
        )
        for i in range(3)
    ]


def mostrar_resultado_sistema(res):
    col1, col2 = st.columns(2)
    col1.metric("Iteraciones", res["iteraciones"])
    col2.metric("Error final", f"{res['error']:.2e}")
    sol = res["solucion"]
    st.success(
        f"x₁ = {sol[0]:.8f}   x₂ = {sol[1]:.8f}   x₃ = {sol[2]:.8f}"
    )
    if not res["converge"]:
        st.warning(
            "El método no convergió en el número máximo de iteraciones."
        )


# ──────────────────────────────────────────
# Tabs
# ──────────────────────────────────────────

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Jacobi", "Gauss-Seidel", "SOR", "Newton-Raphson", "Lagrange"]
)

# ── Jacobi ──
with tab1:
    st.subheader("Método de Jacobi")
    A = input_matriz("j")
    b = input_b("j")
    c1, c2 = st.columns(2)
    tol = c1.number_input(
        "Tolerancia", value=1e-6, format="%.2e", key="j_tol"
    )
    max_iter = c2.number_input(
        "Máx. iteraciones", value=100, step=1, key="j_maxiter"
    )

    if st.button("Calcular", key="btn_jacobi"):
        try:
            if not tiene_diagonal_valida(A):
                st.error(
                    "La diagonal tiene ceros — el método no puede continuar."
                )
            else:
                if not es_diagonal_dominante(A):
                    st.warning(
                        "La matriz no es diagonal dominante, "
                        "puede no converger."
                    )
                res = Jacobi(A, b, tol=tol, max_iter=int(max_iter))
                mostrar_resultado_sistema(res)
        except Exception as e:
            st.error(str(e))

# ── Gauss-Seidel ──
with tab2:
    st.subheader("Método de Gauss-Seidel")
    A = input_matriz("g")
    b = input_b("g")
    c1, c2 = st.columns(2)
    tol = c1.number_input(
        "Tolerancia", value=1e-6, format="%.2e", key="g_tol"
    )
    max_iter = c2.number_input(
        "Máx. iteraciones", value=100, step=1, key="g_maxiter"
    )

    if st.button("Calcular", key="btn_gauss"):
        try:
            if not tiene_diagonal_valida(A):
                st.error(
                    "La diagonal tiene ceros — el método no puede continuar."
                )
            else:
                if not es_diagonal_dominante(A):
                    st.warning(
                        "La matriz no es diagonal dominante, "
                        "puede no converger."
                    )
                res = GaussSeidel(A, b, tol=tol, max_iter=int(max_iter))
                mostrar_resultado_sistema(res)
        except Exception as e:
            st.error(str(e))

# ── SOR ──
with tab3:
    st.subheader("Método SOR")
    A = input_matriz("s")
    b = input_b("s")
    c1, c2, c3 = st.columns(3)
    w = c1.number_input(
        "ω (0, 2)", value=1.2, min_value=0.01, max_value=1.99,
        step=0.1, key="s_w"
    )
    tol = c2.number_input(
        "Tolerancia", value=1e-6, format="%.2e", key="s_tol"
    )
    max_iter = c3.number_input(
        "Máx. iteraciones", value=100, step=1, key="s_maxiter"
    )

    if st.button("Calcular", key="btn_sor"):
        try:
            if not tiene_diagonal_valida(A):
                st.error(
                    "La diagonal tiene ceros — el método no puede continuar."
                )
            else:
                if not es_diagonal_dominante(A):
                    st.warning(
                        "La matriz no es diagonal dominante, "
                        "puede no converger."
                    )
                res = SOR(A, b, w=w, tol=tol, max_iter=int(max_iter))
                mostrar_resultado_sistema(res)
        except Exception as e:
            st.error(str(e))

# ── Newton-Raphson ──
with tab4:
    st.subheader("Newton-Raphson 2×2")
    st.caption(
        "Usa `x` e `y` como variables. Ejemplo: `x**2 + y - 1`"
    )

    c1, c2 = st.columns(2)
    f_str = c1.text_input("f(x, y)", value="x**2 + y - 1")
    g_str = c2.text_input("g(x, y)", value="x + y**2 - 1")
    dfdx_s = c1.text_input("∂f/∂x", value="2*x")
    dfdy_s = c2.text_input("∂f/∂y", value="1")
    dgdx_s = c1.text_input("∂g/∂x", value="1")
    dgdy_s = c2.text_input("∂g/∂y", value="2*y")

    c1, c2 = st.columns(2)
    x0 = c1.number_input("x₀", value=0.5)
    y0 = c2.number_input("y₀", value=0.5)
    c1, c2 = st.columns(2)
    tol_n = c1.number_input(
        "Tolerancia", value=1e-6, format="%.2e", key="n_tol"
    )
    max_iter_n = c2.number_input(
        "Máx. iteraciones", value=100, step=1, key="n_maxiter"
    )

    if st.button("Calcular", key="btn_newton"):
        try:
            _env = {"__builtins__": {}, "abs": abs}

            def make_fn(expr):
                return lambda x, y: eval(
                    expr, {**_env, "x": x, "y": y}
                )

            res = NewtonRaphson2x2(
                f=make_fn(f_str),
                g=make_fn(g_str),
                df_dx=make_fn(dfdx_s),
                df_dy=make_fn(dfdy_s),
                dg_dx=make_fn(dgdx_s),
                dg_dy=make_fn(dgdy_s),
                x0=x0,
                y0=y0,
                tol=tol_n,
                max_iter=int(max_iter_n),
            )
            sol = res["solucion"]
            c1, c2 = st.columns(2)
            c1.metric("Iteraciones", res["iteraciones"])
            c2.metric(
                "Error final",
                f"{res['error']:.2e}" if res["error"] else "N/A",
            )
            st.success(f"x = {sol[0]:.10f}   y = {sol[1]:.10f}")
            if not res["converge"]:
                st.warning(res.get("mensaje", "No convergió."))
        except Exception as e:
            st.error(f"Error al evaluar las expresiones: {e}")

# ── Lagrange ──
with tab5:
    st.subheader("Interpolación de Lagrange")

    n_pts = st.number_input(
        "Número de puntos", min_value=2, max_value=10, value=4, step=1
    )
    st.markdown("**Puntos (x, y)**")

    x_vals, y_vals = [], []
    cols = st.columns(2)
    for i in range(int(n_pts)):
        xv = cols[0].number_input(
            f"x{i+1}", value=float(i + 1), key=f"lx{i}"
        )
        yv = cols[1].number_input(
            f"y{i+1}", value=float((i + 1) ** 2), key=f"ly{i}"
        )
        x_vals.append(xv)
        y_vals.append(yv)

    x_eval = st.number_input("Evaluar en x =", value=2.5)

    if st.button("Interpolar", key="btn_lagrange"):
        try:
            resultado = InterpolacionLagrange(x_vals, y_vals, x_eval)
            st.success(f"P({x_eval}) = {resultado:.10f}")
            st.caption(
                f"Polinomio de grado {int(n_pts) - 1} "
                f"con {int(n_pts)} puntos"
            )
        except Exception as e:
            st.error(str(e))
