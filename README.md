# Calculadora de Métodos Numéricos

Una aplicación interactiva para resolver sistemas de ecuaciones y problemas numéricos usando diferentes métodos.

## Métodos Disponibles

1. **Jacobi** - Método iterativo para sistemas lineales
2. **Gauss-Seidel** - Método iterativo mejorado
3. **SOR** - Successive Over-Relaxation
4. **LU** - Descomposición LU con pivoteo parcial
5. **Newton-Raphson** - Método para sistemas no lineales 2×2
6. **Lagrange** - Interpolación polinómica

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. **Clonar o descargar el proyecto**

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

## Ejecución

### Opción 1: Archivo ejecutable (Recomendado)

**En Windows:**
- Haz doble clic en `run.bat`

**En Mac/Linux:**
- Abre terminal en la carpeta del proyecto
- Ejecuta: `chmod +x run.sh && ./run.sh`

### Opción 2: Comando manual

Ejecuta la aplicación con:

```bash
streamlit run ui/Menu.py
```

La aplicación se abrirá en tu navegador en `http://localhost:8501`

## Uso

### Métodos Lineales (Jacobi, Gauss-Seidel, SOR, LU)

1. Ingresa los valores de la matriz A (3×3)
2. Ingresa el vector b (3 elementos)
3. Configura parámetros (tolerancia, máx. iteraciones)
4. Haz clic en "Calcular"

### Newton-Raphson

1. Ingresa dos funciones f(x,y) y g(x,y)
2. Ingresa sus derivadas parciales
3. Establece valores iniciales x₀ e y₀
4. Haz clic en "Calcular"

**Funciones soportadas:** `exp`, `log` (ln), `sqrt`, `sin`, `cos`, `tan`, `pi`, `e`

**Ejemplo:**
- f(x,y) = `exp(x) + y - 1`
- g(x,y) = `x + log(y) - 1`

### Lagrange

1. Ingresa número de puntos
2. Proporciona coordenadas (x, y)
3. Especifica el valor x donde evaluar
4. Haz clic en "Interpolar"

## Estructura del Proyecto

```
.
├── methods/              # Implementación de métodos
│   ├── Jacobi.py
│   ├── GaussSeidel.py
│   ├── SOR.py
│   ├── LU.py
│   ├── NewtonRaphson.py
│   ├── Interpolacion.py
│   └── __init__.py
├── ui/                   # Interfaz de usuario
│   ├── Menu.py
│   └── __init__.py
├── utils/                # Funciones auxiliares
│   ├── Validaciones.py
│   └── __init__.py
├── requirements.txt      # Dependencias
└── README.md            # Este archivo
```

## Notas

- Los métodos iterativos requieren que la matriz sea diagonal dominante para garantizar convergencia
- El método LU no requiere esta condición
- Newton-Raphson necesita buenas aproximaciones iniciales para converger
