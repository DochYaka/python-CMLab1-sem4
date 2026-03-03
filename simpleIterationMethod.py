import numpy as np
import function


def _build_phi(a, b, n=4000):
    xs = np.linspace(a, b, n)
    df_vals = function.df(xs)

    mid = (a + b) / 2
    s = np.sign(function.df(mid))
    if s == 0:
        s = 1

    max_abs_df = np.max(np.abs(df_vals))
    lam0 = -s / max_abs_df

    safety = 1.0
    while True:
        lam = lam0 / safety
        
        q = np.max(np.abs(1 + lam * df_vals))
        if q < 1:
            break
        safety *= 1.25
        if safety > 1e6:
            raise RuntimeError("Не получилось подобрать lambda, чтобы q<1")

    def phi(x):
        return x + lam * function.f(x)

    return phi, lam, q


def simple_iteration_method(a, b, eps_x=1e-4, eps_f=1e-3, max_iter=100, x0=None):
    if x0 is None:
        x0 = (a + b) / 2

    phi, lam, q = _build_phi(a, b)

    print("Метод простых итераций")
    print(f"lambda = {lam:.10g}")

    print("Эквивалентная форма уравнения:")
    print(f"x = x + ({lam:.10g}) * f(x)")

    print(f"q = {q:.6g}")
    print(f"Интервал [{a}, {b}]")
    print(f"Старт x0 = {x0:.10f}")
    print("=" * 40)

    x = x0
    print(f"итерация {0:3d}: x = {x:.10f}")

    for i in range(1, max_iter + 1):
        x_next = phi(x)

        if not (a <= x_next <= b):
            print(f"Вышли за отрезок на итерации {i}: x = {x_next:.10f}")
            print()
            return None

        print(f"итерация {i:3d}: x = {x_next:.10f}")

        diff = abs(x_next - x)

        x_ok = False
        if q <= 0.5:
            if diff < eps_x:
                x_ok = True
        else:
            if (q / (1 - q)) * diff < eps_x:
                x_ok = True

        f_ok = abs(function.f(x_next)) < eps_f

        if x_ok and f_ok:
            print("=" * 40)
            print(f"Корень: x ≈ {x_next:.10f}")
            print(f"f(x) = {function.f(x_next):.10e}")
            print()
            return x_next

        x = x_next
    
    print("Не сошлось за max_iter")
    print()
    return None
