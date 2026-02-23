import matplotlib.pyplot as plt
import numpy as np
import function

def Graph():
    x = np.linspace(-6, 6, 1000)

    # ----- График f(x) -----
    plt.figure()
    plt.plot(x, function.f(x))
    plt.axhline(0)
    plt.title("График функции f(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.show()

    # ----- График f'(x) -----W
    plt.figure()
    plt.plot(x, function.df(x))
    plt.axhline(0)
    plt.title("График первой производной f'(x)")
    plt.xlabel("x")
    plt.ylabel("f'(x)")
    plt.grid(True)
    plt.show()

    # ----- График f''(x) -----
    plt.figure()
    plt.plot(x, function.d2f(x))
    plt.axhline(0)
    plt.title("График второй производной f''(x)")
    plt.xlabel("x")
    plt.ylabel("f''(x)")
    plt.grid(True)
    plt.show()