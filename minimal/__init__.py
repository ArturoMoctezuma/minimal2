import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


def my_sum(x, y):
    """A function that sums. """
    return x+y


def my_mul(x, y):
    """A function that multiply. """
    return x*y


def grafica_funcion(expr):
    figure = plt.figure()
    x = sp.Symbol('x')
    f = sp.sympify(expr)
    f_numeric = sp.lambdify(x, f)

    ax = figure.add_subplot(2, 1, 1)
    ax2 = figure.add_subplot(2, 1, 2)

    x_vals = np.linspace(-5, 5, 100)
    ax.plot(x_vals, f_numeric(x_vals), label="Función")
    ax.legend()

    df = sp.diff(f)
    df_numeric = sp.lambdify(x, df)

    ax2.plot(x_vals, df_numeric(x_vals), label='Derivada')
    ax2.legend()

    plt.show()
