import math

# Функция для вычисления значения введенной пользователем функции
def user_function(x, func_str):
    try:
        # Замена 'sqrt' на 'math.sqrt' и '^' на '**' в строке функции
        func_str = func_str.replace('sqrt', 'math.sqrt').replace('^', '**')
        return eval(func_str)
    except Exception as e:
        print(f"Ошибка при вычислении функции: {e}")
        return None

# Метод трапеций
def trapezoidal_method(f, a, b, n):
    h = (b - a) / n  # Шаг
    x = [a + i * h for i in range(n + 1)]  # Точки разбиения
    y = [f(xi) for xi in x]  # Значения функции в этих точках
    integral = h * (0.5 * y[0] + 0.5 * y[-1] + sum(y[1:-1]))  # Формула метода трапеций
    return integral

# Запрос у пользователя данных
func_str = input("Введите функцию для интегрирования (например, 'sin(x)', 'x**2'): ")
a = float(input("Введите начало интервала (a): "))
b = float(input("Введите конец интервала (b): "))
n = int(input("Введите число разбиений (n): "))

# Вычисления для метода трапеций
trapezoidal_result = trapezoidal_method(lambda x: user_function(x, func_str), a, b, n)

# Вывод результатов
print(f"Метод трапеций для n = {n}: {trapezoidal_result:.6f}")
import math

# Функция для вычисления значения введенной пользователем функции
def user_function(x, func_str):
    try:
        # Замена 'sqrt' на 'math.sqrt', 'cos' на 'math.cos', и '^' на '**' в строке функции
        func_str = func_str.replace('sqrt', 'math.sqrt').replace('cos', 'math.cos').replace('^', '**')
        return eval(func_str)
    except Exception as e:
        print(f"Ошибка при вычислении функции: {e}")
        return None

# Метод Симпсона
def simpson_method(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Число разбиений n должно быть четным для метода Симпсона")
    h = (b - a) / n  # Шаг
    x = [a + i * h for i in range(n + 1)]  # Точки разбиения
    y = [f(xi) for xi in x]  # Значения функции в этих точках
    integral = (h / 3) * (y[0] + 4 * sum(y[i] for i in range(1, n, 2)) + 2 * sum(y[i] for i in range(2, n-1, 2)) + y[-1])  # Формула Симпсона
    return integral

# Запрос у пользователя данных
func_str = input("Введите функцию для интегрирования (например, 'sin(x)', 'x**2'): ")
a = float(input("Введите начало интервала (a): "))
b = float(input("Введите конец интервала (b): "))
n = int(input("Введите число разбиений (n): "))

# Проверка, чтобы n было четным для метода Симпсона
if n % 2 != 0:
    print("Для метода Симпсона число разбиений должно быть чётным. Уменьшаем n на 1.")
    n -= 1

# Вычисления для метода Симпсона
simpson_result = simpson_method(lambda x: user_function(x, func_str), a, b, n)

# Вывод результатов
print(f"Метод Симпсона для n = {n}: {simpson_result:.6f}")