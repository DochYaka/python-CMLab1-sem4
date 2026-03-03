import function

def secant_method(x0, x1, eps=1e-4, max_iter=100):
  
    print(f"\nНачальные приближения: x0 = {x0}, x1 = {x1}")
    
    for i in range(max_iter):
        f_x0 = function.f(x0)
        f_x1 = function.f(x1)
        
        # Проверка на деление на ноль
        if abs(f_x1 - f_x0) < 1e-10:
            print("Слишком близкие значения функции")
            return None
        
        # Формула метода секущих
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
        print(f"Итерация {i+1}: x = {x2}")
        
        # Проверка точности
        if abs(x2 - x1) < eps:
            print("Корень найден:", x2)
            return x2
        
        # Переприсваивание для следующей итерации
        x0, x1 = x1, x2
    
    print("Метод не сошёлся")
    return None
