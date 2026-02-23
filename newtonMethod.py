import function

def newton_method(a, b, eps=1e-4, max_iter=100):
    x = (a + b) / 2

    print("Метод Ньютона")
    print(f"Начальное приближение x0 = {x:.6f}")
    print("=" * 40)

    for i in range(1, max_iter + 1):
        fx = function.f(x)
        dfx = function.df(x)

        if abs(dfx) < 1e-10:
            print("Производная слишком мала, метод остановлен")
            break

        x_new = x - fx / dfx

        print(f"Итерация {i}: x = {x_new:.6f}")

        if abs(x_new - x) < eps:
            print("=" * 40)
            print(f"Корень найден: x ≈ {x_new:.6f}")
            print()
            return x_new

        x = x_new

    print("Метод не сошёлся за заданное число итераций")
    return None