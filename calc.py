import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Ошибка: деление на 0"

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Ошибка: извлечение корня из отрицательного числа"

def factorial(x):
    if x < 0:
        return "Ошибка: факториал отрицательного числа не определен"
    elif x == 0:
        return 1
    else:
        return x * factorial(x - 1)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def get_number_input():
    while True:
        try:
            return float(input("Введите число: "))
        except ValueError:
            print("Ошибка: введите корректное число.")

def get_operation():
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '**': power,
        'sqrt': square_root,
        'fact': factorial,
        'sin': sin,
        'cos': cos,
        'tan': tan
    }

    while True:
        operation = input("Выберите операцию (+, -, *, /, **, sqrt, fact, sin, cos, tan): ")
        if operation in operations:
            return operations[operation]
        else:
            print("Ошибка: некорректная операция.")

if __name__ == "__main__":
    try:
        x = get_number_input()
        operation = get_operation()

        if operation in {square_root, factorial, sin, cos, tan}:
            result = operation(x)
            print(f"Результат: {result}")
        else:
            y = get_number_input()
            result = operation(x, y)
            print(f"Результат: {result}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")