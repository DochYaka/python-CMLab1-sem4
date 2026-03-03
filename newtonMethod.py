import function

def newton_method(a, b, eps=1e-4, max_iter=100):

    print("Метод Ньютона")
    print(f"Интервал: [{a}, {b}]")
    print(f"Начальное приближение x0 = {x:.6f}")
    print("=" * 40)

    print(f"\nНачальное приближение x0 = {x}")

    for i in range(max_iter):
        fx = function.f(x)
        dfx = function.df(x)

        if abs(dfx) < 1e-10:
            print("Производная близка к нулю")
            return None

        x_new = x - fx / dfx
        print(f"Итерация {i+1}: x = {x_new}")

        if abs(x_new - x) < eps:
            print("Корень найден:", x_new)
            return x_new

        x = x_new

    print("Метод не сошёлся")
    return None