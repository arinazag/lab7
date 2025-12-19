def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def taylor_sin(x, terms=13):
    result = 0
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)
        result += term
    return result

def taylor_cos(x, terms=13):
    result = 0
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)
        result += term
    return result

def taylor_ln(x, terms=25):
    """Натуральный логарифм через ряд Тейлора"""
    if x <= 0:
        raise ValueError("Логарифм только для положительных чисел")

    z = (x - 1) / (x + 1)
    result = 0
    for n in range(terms):
        term = (2 * z ** (2 * n + 1)) / (2 * n + 1)
        result += term
    return result

def abs_value(x):
    return -x if x < 0 else x

def taylor_sqrt(x, iterations=10):
    if x < 0:
        raise ValueError("Квадратный корень из отрицательного числа")
    if x == 0:
        return 0

    guess = x / 2
    for i in range(iterations):
        guess = (guess + x / guess) / 2
    return guess

def main_function(x):
    """
    Главная функция:
    f(x) = sqrt(sin(x) * cos(ln(|x|))) если x ≤ 0
    f(x) = (1 - cos(x)) / sin(x) если x > 0
    """
    if x <= 0:
        sin_val = taylor_sin(x)
        abs_val = abs_value(x)

        if abs_val == 0:
            raise ValueError("Неопределено для x = 0")
        
        ln_val = taylor_ln(abs_val)
        cos_val = taylor_cos(ln_val)

        product = sin_val * cos_val

        if product < 0 and abs(product) < 1e-10:
            product = 0

        if product < 0:
            raise ValueError("Квадратный корень из отрицательного числа")

        return taylor_sqrt(product)

    else:
        # Для x > 0
        sin_val = taylor_sin(x)
        cos_val = taylor_cos(x)

        if abs(sin_val) < 1e-10:
            raise ValueError("Деление на ноль")

        return (1 - cos_val) / sin_val